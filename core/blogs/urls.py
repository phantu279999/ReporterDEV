from django.urls import path

from core.blogs import views

app_name = 'blog'


urlpatterns = [
	path('', views.list_blog_view, name='list_blog'),
	path('detail/<slug:slug>/', views.detail_blog_view, name='detail_blog'),
]