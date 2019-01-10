from django.contrib import admin

from .models import ProfileModel


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'info', 'location',)
    list_filter = ('location',)
    ordering = ('-user',)
    search_fields = ('user', 'info', 'location',)


admin.site.register(ProfileModel, ProfileAdmin)
