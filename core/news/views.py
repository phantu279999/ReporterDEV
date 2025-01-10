from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import News, Zone, NewsInZone, TagNews


def news_in_zone(request, url):
	zones = Zone.objects.all()
	news_zone = NewsInZone.objects.filter(zone__url=url)
	zone = news_zone.select_related('zone')[0].zone
	news = [item.news for item in news_zone.select_related('news')]
	# news = News.objects.filter(newsinzone__zone__url=url).distinct()
	return render(request, 'news/news_in_zone.html', {'zones': zones, 'zone': zone, 'news': news})


def list_news_view(request):
	zones = Zone.objects.all()
	news = News.objects.all()

	news_focus = news.filter(is_focus=True)[:3]
	return render(
		request,
		'news/list_news.html',
		{'zones': zones, 'news': news, 'news_focus': news_focus}
	)


def detail_news_view(request, slug):
	new = get_object_or_404(News, slug=slug)
	tagnews = TagNews.objects.filter(news_id=new.id).select_related('tag')
	newsinzone = new.newsinzone_set.select_related('zone').prefetch_related('zone__newsinzone_set__news')
	news_in_zone = set(
		news_in_zone_item.news
		for zone_news in newsinzone
		for news_in_zone_item in zone_news.zone.newsinzone_set.all()
	)
	tag_in_news = [item.tag for item in tagnews]
	return render(request, 'news/detail_news.html', {
		'new': new,
		'tag_in_news': tag_in_news,
		'news_in_zone': list(news_in_zone)
	})


def news_in_tag(request, url):
	tagnews = TagNews.objects.filter(tag__url=url)
	tag = tagnews.select_related('tag')[0].tag
	news = [item.news for item in tagnews.select_related('news')]

	paginator = Paginator(news, 10)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	ctx = {
		'tag': tag,
		'page_obj': page_obj
	}
	return render(request, 'news/news_in_tag.html', context=ctx)
