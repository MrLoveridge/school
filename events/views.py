from datetime import datetime, timedelta
from django.shortcuts import render
from .models import Event

# Create your views here.

def index(request):

    all_events = Event.objects.all().order_by('date')

    events_DTG = all_events.filter(title__contains = 'DTG')

    events_today = all_events.filter(date = datetime.now())

    context = {'all_events':all_events, 'events_DTG':events_DTG, 'events_today':events_today}
    
    return render(request, 'events/index.html', context)