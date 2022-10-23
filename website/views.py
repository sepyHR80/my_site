from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_home(request):
    return render(request , 'websites/index.html')

def contact_view(request):
    return render(request , 'websites/contact.html')

def about_view(request):
    return render(request, 'websites/about.html')

