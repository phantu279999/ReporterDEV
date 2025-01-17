from django.urls import path, include

from . import views

# app_name = 'api'

urlpatterns = [
    path('news/', views.NewsView.as_view(), name='news'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='detail_news'),
]

urlpatterns += [
    path('auth/', include('rest_framework.urls')),
]
