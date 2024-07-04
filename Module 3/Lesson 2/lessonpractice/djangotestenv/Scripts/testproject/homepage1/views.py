from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def homepage(request):
    context= {}

    return render(request, 'homepage.html')