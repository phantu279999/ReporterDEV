from django.shortcuts import render

from core.news.models import News


def index(request):
	news = News.objects.all()[:6]
	return render(request, 'index.html', {'news': news})
