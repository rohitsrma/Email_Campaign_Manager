from .thread import *
from .models import Campaign

def send_email(modeladmin, request, queryset):
    # Iterate through the selected campaigns and send emails
    for campaign in queryset:
        # You can add your email sending logic here
        # For example, you can call your `send_email` function from here
        send_email(campaign)
send_email.short_description = "send email"