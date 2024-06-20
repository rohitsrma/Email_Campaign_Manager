from .thread import *
from .models import Campaign

def send_email(modeladmin, request, queryset):
    # Iterate through the selected campaigns and send emails
    for campaign in queryset:
        send_email(campaign)
send_email.short_description = "send email"
