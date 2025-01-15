from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.views import login_required
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse

from . import forms
from .models import AuthorProfile, Author, CustomUser, Follow
from .utils import validate_password


@login_required
def author_profile_view(request):
	profile, created = AuthorProfile.objects.get_or_create(user=request.user)

	if request.method == 'POST':
		form = forms.AuthorProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
	else:
		form = forms.AuthorProfileForm()
	return render(request, 'accounts/profile.html', {'profile': profile, 'form': form})


def other_author_view(request, pk):
	author = get_object_or_404(Author, pk=pk)
	profile, created = AuthorProfile.objects.get_or_create(user=author)

	follow_instance = Follow.objects.filter(follower=request.user, following=author)
	is_following = follow_instance.exists()

	if request.method == 'POST':
		status_follow = request.POST.get('follow', '')
		if status_follow == 'follow':
			Follow.objects.create(follower=request.user, following=author)
		elif status_follow == 'unfollow':
			follow_instance.delete()
		return redirect(reverse('accounts:other_profile', kwargs={'pk': pk}))

	number_follower = Follow.objects.filter(following=author).count()
	return render(request, 'accounts/author_profile.html', {
		'profile': profile,
		'number_follower': number_follower,
		'is_following': is_following,
	})



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

		if CustomUser.objects.filter(email=email).exists():
			messages.error(request, "Email is already registered")
			return render(request, 'accounts/register.html')

		user = CustomUser.objects.create_user(email=email, password=password)
		user.save()

		return redirect('home')

	return render(request, 'accounts/register.html')


@login_required
def logout_view(request):
	logout(request)
	return redirect('home')
