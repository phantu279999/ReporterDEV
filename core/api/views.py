from rest_framework import generics, status
from rest_framework.response import Response


from core.news import models as news_model
from core.blogs import models as blog_model

from .serializers import NewsSerializer
from .permissions import IsAuthor, IsAdmin


class NewsView(generics.ListCreateAPIView):
    queryset = news_model.News.objects.all()
    serializer_class = NewsSerializer

    def get_permissions(self):
        permisson_classes = []
        if self.request.method != 'GET':
            permisson_classes = [IsAuthor]
        return [permisson() for permisson in permisson_classes]


class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = news_model.News.objects.all()
    serializer_class = NewsSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthor]
        return [permission() for permission in permission_classes]
