from django.contrib import admin
from django.urls import path

from .views import category, index

urlpatterns = [
    path('admin', admin.site.urls, name='admin'),
    path('', index, name='home'),
    path('category/<int:category_id>/', category, name='category'),
]
