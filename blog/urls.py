#importiamo i metodi che appartengono a django e a tutte le nostre views dell'app blog
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]