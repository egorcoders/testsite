from django.contrib import admin
from django.urls import path

from .views import add_news, category, index, single_news

urlpatterns = [
    path('admin', admin.site.urls, name='admin'),
    path('', index, name='home'),
    path('category/<int:category_id>/', category, name='category'),
    path('news/<int:news_id>/', single_news, name='single_news'),
    path('add_news/', add_news, name='add_news'),
]
