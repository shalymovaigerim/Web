from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request):
    return render(request,'index.html')

def about(request) :
    return render(request,'about.html')

def mission(request):
    return render(request, 'mission.html')


