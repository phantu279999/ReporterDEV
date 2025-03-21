from rest_framework import serializers
from djoser.serializers import UserSerializer as DjoserUserSerializer

from accounts.models import CustomUser as User
from core.news.models import News, Tag, TagNews
from core.blogs.models import Blog, Category


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TagNewsSerializer(serializers.ModelSerializer):
    tag = TagSerializer()

    class Meta:
        model = TagNews
        fields = ['tag']


class NewsSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = [
            'title',
            'sapo',
            'avatar',
            'news_type',
            'status',
            'slug',
            'content',
            'created_by',
            'edited_by',
            'is_on_home',
            'is_focus',
            'is_pr',
            'tags',
            'author'
        ]

    def get_tags(self, obj):
        tag_new = TagNews.objects.filter(news=obj)
        return TagNewsSerializer(tag_new, many=True).data



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CustomDjoserUserSerializer(DjoserUserSerializer):
    class Meta(DjoserUserSerializer.Meta):
        ref_name = 'DjoserUserSerializer'
