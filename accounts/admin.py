from django.contrib import admin

from .models import Author, AuthorProfile, Reader, CustomUser, Follow

admin.site.register(CustomUser)
admin.site.register(Author)
admin.site.register(Reader)
admin.site.register(AuthorProfile)
admin.site.register(Follow)
