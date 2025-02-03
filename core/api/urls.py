from django.urls import path, include, re_path
from django.conf import settings
from rest_framework.authtoken import views as view_auth
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from . import views

router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('users', views.UserViewSet)
router.register('categories', views.CategoryViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title='Reporter Developer API',
        default_version='v1',
        description='API for Reporter developer'
    ),
    url=settings.API_URL,
    public=True,
    permission_classes=[permissions.IsAuthenticated] if not settings.DEBUG else [],
)


urlpatterns = [
    path('news/', views.NewsView.as_view(), name='api_news'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='api_detail_news'),
    path('blog/', views.BlogListView.as_view(), name='api_blog'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='api_detail_blog'),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path("token-auth/", view_auth.obtain_auth_token),
    re_path(
        r"^swagger(?P<swagger_format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
