from collections.abc import Callable, Iterable, Mapping
from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Subscribe, UnsubscribedUser, Campaign
from .utils import send_campaign
from django.core.mail import send_mail
from .thread import EmailThread

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')

        subscriber, created = Subscribe.objects.get_or_create(email=email)
        subscriber.name = name
        subscriber.save()

        return JsonResponse({'message': 'Subscriber added successfully.'})
    else:
        return render(request, 'subscribe.html')


def unsubscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            subscriber = Subscribe.objects.get(email=email)
            unsubscribed_user, created = UnsubscribedUser.objects.get_or_create(subscriber=subscriber)
            subscriber.is_active = False 
            subscriber.save()
            unsubscribed_user.is_active = True 
            unsubscribed_user.save()

            return JsonResponse({'message': 'User unsubscribed successfully.'})
        except Subscribe.DoesNotExist:
            return JsonResponse({'message': 'Subscriber not found.'})
    else:
        return render(request, 'unsubscribe.html')
    
def send_email(request):
    campaign = Campaign.objects.get(pk=3)
    EmailThread(send_campaign, campaign).start()
    return JsonResponse({'message': 'Email sent successfully!!'})