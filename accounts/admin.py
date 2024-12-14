from django.contrib import admin

from .models import Author, AuthorProfile, Reader, CustomUser

admin.site.register(CustomUser)
admin.site.register(Author)
admin.site.register(Reader)
admin.site.register(AuthorProfile)
