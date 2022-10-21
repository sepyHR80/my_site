from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_home(request):
    return HttpResponse("hello world")

def contact_view(request):
    return HttpResponse({'sepehr':'heidari'})

def about_view(request):
    return HttpResponse({'sepehr':'heidari'})

