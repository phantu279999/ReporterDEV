from django.urls import path

from core.blogs import views

app_name = 'blog'


urlpatterns = [
	path('', views.BlogListView.as_view(), name='list_blog'),
	path('detail/<slug:slug>/', views.DetailBlogView.as_view(), name='detail_blog'),
]