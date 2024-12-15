from django.shortcuts import render

from .models import News, Zone, NewsInZone


def news_in_zone(request, url):
	news_zone = NewsInZone.objects.filter(zone__url=url)
	zone = news_zone.select_related('zone')[0].zone
	news = [item.news for item in news_zone.select_related('news')]
	# news = News.objects.filter(newsinzone__zone__url=url).distinct()
	return render(request, 'news/news_in_zone.html', {'zone': zone, 'news': news})


def list_news_view(request):
	zones = Zone.objects.all()
	news = News.objects.all()

	return render(
		request,
		'news/list_news.html',
		{'zones': zones, 'news': news}
	)


def detail_news_view(request, slug):
	new = News.objects.get(slug=slug)

	return render(request, 'news/detail_news.html', {'new': new})
