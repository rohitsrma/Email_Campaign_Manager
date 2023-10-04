from django.contrib import admin
from .models import Subscribe, UnsubscribedUser, Campaign
from .process import *
# Register your models here.

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_active')

class UnsubscribedUserAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'is_active')

admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(UnsubscribedUser, UnsubscribedUserAdmin)

class CampaignAdmin(admin.ModelAdmin):
    actions = ['send_selected_campaigns_email']

    def send_selected_campaigns_email(self, request, queryset):
        for campaign in queryset:
            send_campaign(campaign)
        self.message_user(request, f'Sent emails for {queryset.count()} campaigns.')

    send_selected_campaigns_email.short_description = "Send Email for selected campaigns"

admin.site.register(Campaign, CampaignAdmin)