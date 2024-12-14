from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import login_required
from django.contrib.auth import login, logout, authenticate

from . import models
from .utils import validate_password


@login_required
def author_profile_view(request):
	try:
		profile = models.AuthorProfile.objects.get(user=request.user)
	except models.AuthorProfile.DoesNotExist:
		profile = None
	return render(request, 'accounts/profile.html', {'profile': profile})


def login_view(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(request=request, email=email, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, "Invalid email or password")
	return render(request, 'accounts/login.html')


def register_view(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		password_confirm = request.POST['password_confirm']

		password_error = validate_password(password, password_confirm)
		if password_error:
			messages.error(request, password_error)
			return render(request, 'accounts/register.html')

		if models.CustomUser.objects.filter(email=email).exists():
			messages.error(request, "Email is already registered")
			return render(request, 'accounts/register.html')

		user = models.CustomUser.objects.create_user(email=email, password=password)
		user.save()

		return redirect('home')

	return render(request, 'accounts/register.html')


@login_required
def logout_view(request):
	logout(request)
	return redirect('home')
