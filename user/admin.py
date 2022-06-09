from django.contrib import admin
from .models import User, Store, Payout


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email')

class StoreAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'store_owner', 'industry')

class PayoutAdmin(admin.ModelAdmin):
    list_display = ('store', 'date', 'amount', 'status', 'store_bank')

admin.site.register(User, UserAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Payout, PayoutAdmin)