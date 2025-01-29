from django.urls import path, include, re_path
from rest_framework.authtoken import views as view_auth
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title='Reporter Developer API',
        default_version='v1',
        description='API for Reporter developer'
    ),
    url="http://localhost:8000/api/v1/",
    public=True,
)


urlpatterns = [
    path('news/', views.NewsView.as_view(), name='api_news'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='api_detail_news'),
]

urlpatterns += [
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
