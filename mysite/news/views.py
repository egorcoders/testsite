from django.http import HttpResponse

from .models import News


def index(request):
    news = News.objects.all()
    ans = '<h1>Список новостей</h1>\n'
    for n in news:
        ans += f'<div><p>{n.title}</p><p>{n.context}</p></div><hr>'
    return HttpResponse(ans)


def latest(request):
    return HttpResponse('latest news')
