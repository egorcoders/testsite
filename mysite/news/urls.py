from django.urls import path

from .views import index, latest

urlpatterns = [
    path('', index),
    path('latest/', latest),
]
