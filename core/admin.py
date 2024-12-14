from django.contrib import admin

from core.news.models import News, NewsInZone, Zone, Tag, TagNews


class NewsAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('slug',)


admin.site.register(Zone)
admin.site.register(News, NewsAdmin)
admin.site.register(Tag)
admin.site.register(NewsInZone)
admin.site.register(TagNews)
