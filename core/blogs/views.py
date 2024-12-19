from django.shortcuts import render

from core.blogs.models import Blog


def list_blog_view(request):
	blogs = Blog.objects.all()
	return render(request, 'blogs/list_blogs.html', {'blogs': blogs})


def detail_blog_view(request, slug):
	blog = Blog.objects.get(slug=slug)
	return render(request, 'blogs/detail_blog.html', {'blog': blog})
