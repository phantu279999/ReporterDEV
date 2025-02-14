from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from .models import News, Zone, NewsInZone, TagNews
from .forms import CommentForm, NewsForm, NewsInZoneFormSet, TagNewsFormSet


def list_news_view(request):
    zones = Zone.objects.all()
    news = News.objects.all()
    if 'search' in request.GET and request.GET['search']:
        return redirect(reverse('news:lastest_news') + f'?keyword={request.GET["search"]}')
    news_focus = news.filter(is_focus=True)[:3]
    return render(
        request,
        'news/list_news.html',
        {'zones': zones, 'news': news[:12], 'news_focus': news_focus}
    )


def news_in_zone(request, url):
    zones = Zone.objects.all()
    news_zone = NewsInZone.objects.filter(zone__url=url)
    zone = news_zone.select_related('zone')[0].zone
    news = [item.news for item in news_zone.select_related('news')]
    # news = News.objects.filter(newsinzone__zone__url=url).distinct()
    return render(request, 'news/news_in_zone.html', {'zones': zones, 'zone': zone, 'news': news})


def detail_news_view(request, slug):
    new = get_object_or_404(News, slug=slug)
    new.increase_view_count()
    tagnews = TagNews.objects.filter(news_id=new.id).select_related('tag')
    newsinzone = new.newsinzone_set.select_related('zone').prefetch_related('zone__newsinzone_set__news')
    news_in_zone = set(
        news_in_zone_item.news
        for zone_news in newsinzone
        for news_in_zone_item in zone_news.zone.newsinzone_set.all()
    )
    tag_in_news = [item.tag for item in tagnews]
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.content_object = new
            comment.creator = request.user
            comment.save()
            return redirect(request.path_info)
    else:
        comment_form = CommentForm()
    return render(request, 'news/detail_news.html', {
        'new': new,
        'tag_in_news': tag_in_news,
        'news_in_zone': list(news_in_zone),
        'comment_form': comment_form
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


def lastest_news_view(request):
    news = News.objects.all()
    if 'keyword' in request.GET:
        news = news.filter(title__icontains=request.GET['keyword'])
    paginator = Paginator(news, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    ctx = {
        'page_obj': page_obj
    }
    return render(request, 'news/lastest_news.html', context=ctx)


# # CRUD for author
# @login_required
# def create_news_view(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         news_in_zone_formset = NewsInZoneFormSet(request.POST, prefix='newsinzone')
#         tag_news_formset = TagNewsFormSet(request.POST, prefix='tagnews')
#         if form.is_valid() and news_in_zone_formset.is_valid() and tag_news_formset.is_valid():
#             news = form.save()
#             news_in_zone_formset.instance = news
#             news_in_zone_formset.save()
#             tag_news_formset.instance = news
#             tag_news_formset.save()
#             return redirect('accounts:profile')
#     else:
#         form = NewsForm()
#         news_in_zone_formset = NewsInZoneFormSet(prefix='newsinzone')
#         tag_news_formset = TagNewsFormSet(prefix='tagnews')
#
#     return render(request, 'news/create_news.html', {
#         'form': form,
#         'newsinzone_formset': news_in_zone_formset,
#         'tagnews_formset': tag_news_formset,
#     })
