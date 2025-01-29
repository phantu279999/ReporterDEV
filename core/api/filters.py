from django_filters import rest_framework as filters

from core.news.models import News


class NewsFilterSet(filters.FilterSet):
    title = filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Title Contains'
    )
    sapo = filters.CharFilter(
        field_name="sapo",
        lookup_expr="icontains",
        label="Sapo Contains",
    )
    content = filters.CharFilter(
        field_name="content",
        lookup_expr="icontains",
        label="Content Contains",
    )

    class Meta:
        model = News
        fields = ["author",]