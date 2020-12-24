from django.urls import path
from . import views

urlpatterns = [
	path('', views.root, name='root'),
	path('dev/', views.dev, name='dev'),
	path('network/', views.network, name='network'),
	path('whoami/', views.whoami, name='whoami'),
	path('ping_me/', views.ping_me, name='ping_me'),
	
]