from django.contrib import admin
from .models import Subscribe, UnsubscribedUser

# Register your models here.

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_active')

class UnsubscribedUserAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'is_active')

admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(UnsubscribedUser, UnsubscribedUserAdmin)