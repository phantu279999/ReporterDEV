from django.shortcuts import render

from core.blogs.models import Blog


def list_blog_view(request):
	blogs = Blog.objects.all()
	return render(request, 'blogs/list_blogs.html', {'blogs': blogs})
