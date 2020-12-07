
from django.urls import path
from . import views
app_name="public"
urlpatterns = [
   
    path('',views.index, name="index"),
    path('about',views.about, name="about"),
    path('mission',views.mission, name="mission"),
    path('grammar',views.grammar, name="grammar"),
    path('vocabulary',views.vocabulary, name="vocabulary"),
    path('food',views.food, name="food"),
    path('animals',views.animals, name="animals"),
    path('clothes',views.clothes, name="clothes"),
    path('different objects',views.differentobjects, name="different objects"),
    path('grammar1',views.grammar1, name="grammar1"),
    path('funfact1', views.funfact1, name="funfact1"),
    
]
