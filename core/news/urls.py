from django.urls import path

from . import views

urlpatterns = [
	path('', views.list_news_view, name='list_news')
]