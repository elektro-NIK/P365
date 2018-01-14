from django.shortcuts import render
from django.views import View


class CalendarView(View):
    @staticmethod
    def get(request):
        return render(request, 'calendar.html', {'title': 'Calendar'})
