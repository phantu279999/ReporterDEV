from django.urls import path, include

from . import views
from core.news import urls as news_urls
from core.blogs import urls as blog_urls

urlpatterns = [
	path('', views.index, name='home'),
	path('news/', include(news_urls)),
	path('blog/', include(blog_urls)),
]
