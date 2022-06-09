from django.contrib import admin
from .models import Schedule

# Register your models here.

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'playlist', 'total_screen', 'date_option', 'hour_option', 'date_created')

admin.site.register(Schedule, ScheduleAdmin)