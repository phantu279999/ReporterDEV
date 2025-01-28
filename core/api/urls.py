from django.urls import path, include
from rest_framework.authtoken import views as view_auth

from . import views


urlpatterns = [
    path('news/', views.NewsView.as_view(), name='api_news'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='api_detail_news'),
]

urlpatterns += [
    path('auth/', include('rest_framework.urls')),
    path("token-auth/", view_auth.obtain_auth_token),
]
