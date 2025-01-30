from django.contrib import admin

from .models import Comment
from core.news.models import News, NewsInZone, Zone, Tag, TagNews
from core.blogs.models import Blog, Category, BlogInCate


class NewsInZoneInline(admin.TabularInline):
	model = NewsInZone
	extra = 1


class TagNewsInline(admin.TabularInline):
	model = TagNews
	extra = 1


class NewsAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'status', 'is_on_home', 'is_focus', 'is_pr')
	search_fields = ('title',)
	list_filter = ('status', 'is_on_home', 'is_focus', 'is_pr')
	inlines = [NewsInZoneInline, TagNewsInline]


class BlogAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'status')
	search_fields = ('title',)
	list_filter = ('status',)


admin.site.register(Zone)
admin.site.register(News, NewsAdmin)
admin.site.register(Tag)
admin.site.register(NewsInZone)
admin.site.register(TagNews)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(BlogInCate)
admin.site.register(Comment)
