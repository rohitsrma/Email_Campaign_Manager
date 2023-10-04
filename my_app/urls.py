from django.contrib import admin
from django.urls import path,include
from my_app import views
from my_app.views import send_email

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('send-email/', send_email, name='send_email'),

]