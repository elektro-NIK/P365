import json
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View

from .models import EventModel


@method_decorator(login_required, name='dispatch')
class CalendarView(View):
    @staticmethod
    def get(request):
        return render(request, 'calendar.html', {'title': 'Calendar', 'active': 'calendar'})


@method_decorator(login_required, name='dispatch')
class DatesEventView(View):
    @staticmethod
    def get(request, id):
        obj = get_object_or_404(EventModel, id=id)
        if (obj.user == request.user or obj.public) and obj.is_active:
            return render(request, '_event-dates.html', {'event': obj})
        return HttpResponseForbidden()


@method_decorator(login_required, name='dispatch')
class GetAllEventsView(View):
    @staticmethod
    def get(request):
        user = User.objects.get(username=request.user.username)
        events = EventModel.objects.filter(user=user, is_active=True)
        result = [{'id': i.id,
                   'name': i.name,
                   'description': i.description,
                   'startDate': i.start_date.isoformat(),
                   'endDate': i.finish_date.isoformat()} for i in events]
        return HttpResponse(json.dumps(result), content_type='application/json')


@method_decorator(login_required, name='dispatch')
class DeleteEventView(View):
    @staticmethod
    def post(request):
        event = EventModel.objects.get(id=request.POST['id'])
        user = User.objects.get(username=request.user.username)
        if event.user == user and event.is_active:
            event.is_active = False
            event.save()
            return HttpResponse(json.dumps('OK'), content_type='application/json')
        else:
            return HttpResponseForbidden()


@method_decorator(login_required, name='dispatch')
class UpdateCreateEventView(View):
    @staticmethod
    def post(request):
        user = User.objects.get(username=request.user.username)
        event_json = json.loads(request.POST['event'])
        start = datetime.strptime(event_json['startDate'][:-5], '%Y-%m-%dT%H:%M:%S')
        finish = datetime.strptime(event_json['endDate'][:-5], '%Y-%m-%dT%H:%M:%S')
        if event_json['id']:                                                                            # Update event
            event = EventModel.objects.get(id=int(event_json['id']))
            if event.user == user and event.is_active:
                event.name = event_json['name']
                event.description = event_json['description']
                event.start_date = timezone.make_aware(start)
                event.finish_date = timezone.make_aware(finish)
            else:
                return HttpResponseForbidden()
        else:                                                                                           # Create event
            event = EventModel(
                name=event_json['name'],
                description=event_json['description'],
                start_date=timezone.make_aware(start),
                finish_date=timezone.make_aware(finish),
                user=user
            )
        event.save()
        return HttpResponse(json.dumps(''), content_type='application/json')
