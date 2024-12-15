from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
	path('', views.list_news_view, name='list_news'),
	path('<slug:slug>/', views.detail_news_view, name='detail_news')
]
