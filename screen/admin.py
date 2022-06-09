from django.contrib import admin

# Register your models here.
from .models import Branch, Videotron, Television

# Register your models here.
class TelevisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'size', 'resolution', 'position', 'monetization_status')

class VideotronAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'resolution', 'address', 'monetization_status')


admin.site.register(Branch)
admin.site.register(Videotron, VideotronAdmin)
admin.site.register(Television, TelevisionAdmin)