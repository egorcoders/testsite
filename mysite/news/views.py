from django.shortcuts import get_object_or_404, render

from .models import Category, News


def index(request):
    news = News.objects.order_by('-published')
    context = {
        'news': news,
    }
    return render(request, 'news/index.html', context)


def category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'news': news,
        'category': category,
    }
    return render(request, 'news/category.html', context)


def single_news(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    context = {'news': news}
    return render(request, 'news/single_news.html', context)
