
from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns =[
	
	#esto es en raiz/polls
	url(r'^$',views.IndexView.as_view(), name='index'),
	#esto es para raiz/polls/5/
	url(r'^specifics/(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name="detail"),
	#esto es para raiz/polls/1/results
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	#esto es para raiz/polls/5/vote
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	#esto es para api
	url(r'^kpis/(?P<client>.+)/(?P<from_date>.+)/(?P<to_date>.+)/$', views.kpis_todas, name='kpis_todas'),
	#esto es para una sola sucursal.
	url(r'^kpis_suc/(?P<client>.+)/(?P<suc>.+)/(?P<from_date>.+)/(?P<to_date>.+)/$', views.kpis_suc, name='kpis_sucursal')
]

