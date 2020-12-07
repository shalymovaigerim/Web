from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request):
    return render(request,'index.html')

def about(request) :
    return render(request,'about.html')

def mission(request):
    return render(request, 'mission.html')

def grammar(request):
    return render(request, "grammar.html")

def vocabulary(request):
    return render(request, "vocabualry.html")

def food(request):
    return render(request, "food.html")

def animals(request):
     return render(request, "animals.html")

# def sizes(request):
#     return render(request, "sizes.html")

# def different objects(request):
#     return render(request, "differentobjects.html")

