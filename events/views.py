from datetime import datetime, timedelta
from django.shortcuts import render, get_object_or_404
from .models import Event

# Create your views here.

def index(request):

    all_events = Event.objects.all().order_by('date')

    events_today = all_events.filter(date = datetime.now())

    context = {'all_events':all_events, 'events_today':events_today}
    
    return render(request, 'events/index.html', context)

def detail(request, event_id):

    event = get_object_or_404(Event, pk=event_id)

    context = {'event': event}

    return render(request, 'events\detail.html', context)