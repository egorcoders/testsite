from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'published', 'updated')
    list_display_links = ('title',)
    search_fields = ('title', 'content')


admin.site.register(News, NewsAdmin)
