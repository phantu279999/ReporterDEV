from django.shortcuts import render

from .models import News


def list_news_view(request):
	news = News.objects.all()

	return render(request, 'news/list_news.html', {'news': news})


def detail_news_view(request, slug):
	new = News.objects.get(slug=slug)

	return render(request, 'news/detail_news.html', {'new': new})
