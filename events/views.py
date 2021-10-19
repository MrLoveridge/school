from datetime import datetime
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

def search(request):

    all_events = Event.objects.all().order_by('date')

    if len(request.GET) == 0:
        relevant_events = all_events
    else:
        search_string = request.GET['q']
        relevant_events = all_events.filter(title__contains = search_string)

    
    context = {'relevant_events':relevant_events}

    return render(request, 'events/search.html', context)














""" print(request)

query_dict = request.GET

if len(query_dict) == 0:
    relevant_events = all_events
else:
    search_string = query_dict['q']
    relevant_events = all_events.filter(title__contains = search_string)

print(relevant_events)

context = {'relevant_events':relevant_events} """