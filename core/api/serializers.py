from rest_framework import serializers

from core.news.models import News

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'

