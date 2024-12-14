from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
	path('profile/', views.author_profile_view, name='profile'),
	path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
	path('register/', views.register_view, name='register'),
]
