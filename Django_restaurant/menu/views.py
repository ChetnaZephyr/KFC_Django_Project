from django.http import HttpResponse
from django.shortcuts import render
from .models import Item
def home(request):
    items=Item.objects.all()
    return render(request, "menu/home.html" , {"items" : items})

def about(request):
    return HttpResponse(
        "<h1?About KFC<h1><p>Welcome to our restaurant.</p>"
    )