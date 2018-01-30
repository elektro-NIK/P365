import json

from datetime import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views import View

from calendar_year.models import EventModel


class CalendarView(View):
    @staticmethod
    def get(request):
        return render(request, 'calendar.html', {'title': 'Calendar', 'active': 'calendar'})


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


class DeleteEventView(View):
    @staticmethod
    def post(request):
        event = EventModel.objects.get(id=request.POST['id'])
        user = User.objects.get(username=request.user.username)
        if event.user == user:
            event.is_active = False
            event.save()
            return HttpResponse(json.dumps(''), content_type='application/json')
        else:
            return HttpResponseForbidden()


class UpdateCreateEventView(View):
    @staticmethod
    def post(request):
        user = User.objects.get(username=request.user.username)
        event_json = json.loads(request.POST['event'])
        if event_json['id']:                                                                            # Update event
            event = EventModel.objects.get(id=int(event_json['id']))
            if event.user == user:
                event.name = event_json['name']
                event.description = event_json['description']
                event.start_date = datetime.strptime(event_json['startDate'], '%Y-%m-%dT%H:%M:%S.%fZ').date()
                event.finish_date = datetime.strptime(event_json['endDate'], '%Y-%m-%dT%H:%M:%S.%fZ').date()
            else:
                return HttpResponseForbidden()
        else:                                                                                           # Create event
            event = EventModel(
                name=event_json['name'],
                description=event_json['description'],
                start_date=datetime.strptime(event_json['startDate'], '%Y-%m-%dT%H:%M:%S.%fZ').date(),
                finish_date=datetime.strptime(event_json['endDate'], '%Y-%m-%dT%H:%M:%S.%fZ').date(),
                user=user
            )
        event.save()
        return HttpResponse(json.dumps(''), content_type='application/json')
