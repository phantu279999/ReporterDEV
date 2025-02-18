from django.shortcuts import render

from core.news.models import News, Tag
from core.blogs.models import Blog


def index(request):
	news = News.objects.all()[:6]
	blogs = Blog.objects.all()[:6]
	tags = Tag.objects.all()[:10]
	context = {
		'news': news,
		'blogs': blogs,
		'tags': tags,
	}
	return render(request, 'index.html', context=context)
