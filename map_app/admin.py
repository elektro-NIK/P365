from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import POIModel, TrackModel

admin.site.register(POIModel, LeafletGeoAdmin)
admin.site.register(TrackModel, LeafletGeoAdmin)
