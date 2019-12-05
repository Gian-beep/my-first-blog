#importiamo i metodi che appartengono a django e a tutte le nostre views dell'app blog
#prende tutto quello che c'è e la trasmette alla view, inoltre specifica che l'url avrà la porala post
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]