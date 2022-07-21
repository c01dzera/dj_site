from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('<h1>Страница приложения women<h1/>')


def categories(request, catid):
    if request.POST:
        print(request.POST)

    return HttpResponse(f'<h1>Категории<h1/><p>{catid}<p/>')


def archive(request, year):
    if int(year) > 2022:
        raise Http404()

    return HttpResponse(f'<h1>Архив по годам<h1/><p>{year}<p/>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1/>')