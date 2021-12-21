from django.shortcuts import render

# Create your views here.

def first(request):
    return render(request, 'menuapp/menu.html')

def add(request):
    return render(request, 'menuapp/add.html')
