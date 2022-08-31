from django.shortcuts import render

from .models import Category, News


def index(request):
    news = News.objects.order_by('-published')
    context = {
        'news': news,
    }
    return render(request, 'news/index.html', context)


def category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
    }
    return render(request, 'news/category.html', context)
