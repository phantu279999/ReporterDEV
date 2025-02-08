from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
	path('', views.list_news_view, name='list_news'),
	path('detail/<slug:slug>/', views.detail_news_view, name='detail_news'),
	path('news-zone/<slug:url>/', views.news_in_zone, name='news_in_zone'),
	path('news-tag/<slug:url>/', views.news_in_tag, name='news_in_tag'),
	path("lastest-news/", views.lastest_news_view, name='lastest_news'),
	# path('create-news/', views.create_news_view, name='create_news'),
]
