from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #code here
    return HttpResponse("Hi you have reached the index page")