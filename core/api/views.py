from django.utils import timezone
from django.db.models import Q
from rest_framework import generics, status, viewsets
from rest_framework.response import Response


from core.news import models as news_model
from core.blogs import models as blog_model

from .serializers import NewsSerializer, TagSerializer
from .permissions import IsAuthor, IsAdmin
from .filters import NewsFilterSet


class NewsView(generics.ListCreateAPIView):
    queryset = news_model.News.objects.all()
    serializer_class = NewsSerializer
    filterset_class = NewsFilterSet

    def get_permissions(self):
        permisson_classes = []
        if self.request.method != 'GET':
            permisson_classes = [IsAuthor, IsAdmin]
        return [permisson() for permisson in permisson_classes]

    # def get(self, request, *args, **kwargs):
    #     print(f"Authorization Header: {request.headers.get('Authorization')}")
    #     print(f"User: {request.user}, Is Authenticated: {request.user.is_authenticated}")
    #     return super().get(request, *args, **kwargs)

    def get_queryset(self):
        base_queryset = news_model.News.objects.all()
        user = self.request.user
        if user.is_anonymous:
            return base_queryset.filter(published_at__lte=timezone.now())
        elif user.user_type == 'admin':
            return base_queryset
        else:
            return base_queryset.filter(Q(author=user))


class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = news_model.News.objects.all()
    serializer_class = NewsSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthor]
        return [permission() for permission in permission_classes]


class TagViewSet(viewsets.ModelViewSet):
    queryset = news_model.Tag.objects.all()
    serializer_class = TagSerializer
