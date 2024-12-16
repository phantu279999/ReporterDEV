from django import forms

from .models import AuthorProfile


class AuthorProfileForm(forms.ModelForm):

	class Meta:
		model = AuthorProfile
		fields = ['bio', 'phone', 'address']
