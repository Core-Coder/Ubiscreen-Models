from django.contrib import admin
from .models import Media, Playlist

# Register your models here.

class MediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'dimension', 'size', 'duration', 'monetization_status')

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'length', 'last_updated', 'date_added')

admin.site.register(Media, MediaAdmin)
admin.site.register(Playlist, PlaylistAdmin)
