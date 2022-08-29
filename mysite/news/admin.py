from django.contrib import admin

from .models import Category, News


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title',
        'content', 'category',
        'is_published', 'updated', 'image'
    )
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_editable = ('is_published',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    list_editable = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
