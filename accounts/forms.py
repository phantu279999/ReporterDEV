from django import forms

from .models import AuthorProfile


class AuthorProfileForm(forms.ModelForm):
	class Meta:
		model = AuthorProfile
		fields = ['full_name', 'bio', 'phone', 'address', 'link_facebook', 'link_x', 'link_other']
