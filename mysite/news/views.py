from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def index(request):
    return HttpResponse('hello')

def latest(request):
    return HttpResponse('latest news')