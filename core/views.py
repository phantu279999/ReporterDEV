from django.shortcuts import render

from core.news.models import News
from core.blogs.models import Blog


def index(request):
	news = News.objects.all()[:6]
	blogs = Blog.objects.all()[:6]
	return render(request, 'index.html', {'news': news, 'blogs': blogs})
