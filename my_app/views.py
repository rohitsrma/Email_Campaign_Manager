from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Subscribe, UnsubscribedUser


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
            subscriber.is_active = False  # Mark the associated Subscribe object as inactive
            subscriber.save()
            unsubscribed_user.is_active = True  # Mark the UnsubscribedUser as active (optional)
            unsubscribed_user.save()

            return JsonResponse({'message': 'User unsubscribed successfully.'})
        except Subscribe.DoesNotExist:
            return JsonResponse({'message': 'Subscriber not found.'})
    else:
        return render(request, 'unsubscribe.html')
