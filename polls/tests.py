from django.test import TestCase

# Create your tests here.
from django.utils import timezone 
from .models import Question
import datetime
import pandas as pd
import json
import requests

class QuestionMethodTests(TestCase):

	def test_was_published_recently_with_future_question(self):
    	
    		time = timezone.now() + datetime.timedelta(days=30)
        	future_question = Question(pub_date=time)
        	self.assertIs(future_question.was_published_recently(), False)

class checarlaapiTests(TestCase):
	def test_checaapi(self):

			url_api = "http://api1.klustera.com:8000/visitantes_dia?client=Pacifico&from=2016-11-24&to=2016-12-31"
			response = requests.get(url_api).json()
			df = pd.DataFrame(response['results'])
			print(df.head(5))
			haydatos = df['cliente'].count()+1 > 0
			self.assertTrue(haydatos)