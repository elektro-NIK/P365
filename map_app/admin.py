from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import POI, Track

admin.site.register(POI, LeafletGeoAdmin)
admin.site.register(Track, LeafletGeoAdmin)
