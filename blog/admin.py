#Aggiungere,modificare,cancellare il post che abbiamo strutturato
from django.contrib import admin
from .models import Post
#permette di essere visibile alla pagina di admin
admin.site.register(Post)
