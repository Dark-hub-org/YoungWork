from django.urls import path

from . import api

urlpatterns = [
    path('not/', api.notifications, name='notifications'),
    path('read/<uuid:pk>/', api.read_notification, name='read_notification'),
]
