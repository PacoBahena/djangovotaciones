
from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns =[
	
	#esto es en raiz/polls
	url(r'^$',views.index, name='index'),
	#esto es para raiz/polls/5/
	url(r'^specifics/(?P<question_id>[0-9]+)/$',views.detail, name="detail"),
	#esto es para raiz/polls/1/results
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	#esto es para raiz/polls/5/vote
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

