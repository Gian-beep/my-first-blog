from django.shortcuts import render

#e' stato creato un metodo post_list che prende request e restituisce un metodo render che fornirà il nostro template
def post_list(request):
    return render(request, 'blog/post_list.html', {})