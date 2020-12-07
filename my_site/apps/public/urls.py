
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
    # path('sizes',views.sizes, name="sizes"),
    # path('differentobjects',views.differentobjects, name="different objects"),
    
]
