from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import Question, Choice
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic

import pandas as pd
import requests
import json

class IndexView(generic.ListView):

	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	
	def get_queryset(self):
		#"return last 3 published questions"
		return Question.objects.order_by('-pub_date')[:2]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):

		context = { 'question': question, 'error_message': 'You did not select a choice mijo'}

		return render(request,'polls/detail.html', context)

	else:

		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def kpis(request,client,from_date,to_date):
	url_api = "http://api1.klustera.com:8000/visitantes_dia?client={}&from={}&to={}".format(client,from_date,to_date)
	#df = pd.read_json(url_api)
	response = requests.get(url_api).json()
	#results = response['results'][:5]
	df = pd.DataFrame(response['results']).to_html()
	return HttpResponse(df)
	 
	 #url_api = "http://api1.klustera.com:8000/visitantes_dia?client=Pacifico&from=2016-11-24&to=2016-12-31"


# def index(request):

# 	latest_question_list = Question.objects.order_by('-pub_date')[:2]
# 	context = {'latest_question_list': latest_question_list}
# 	return render(request,'polls/index.html',context)



# def detail(request, question_id):
	
# 	try:
# 		question = Question.objects.get(pk=question_id)
# 	except Question.DoesNotExist:
# 		raise Http404('Question does not exist')
		
# 	context = {'question' : question}
# 	return render(request,'polls/detail.html',context)




# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})








