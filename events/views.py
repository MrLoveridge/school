from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

# Create your views here.

def index(request):

    all_events = Event.objects.all()

    context = {'all_events':all_events}
    
    return render(request, 'events/index.html', context)