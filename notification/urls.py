from django.urls import path

from . import api

urlpatterns = [
    path('read/<str:pk>/', api.read_notification, name='read_notification'),
    path('notes/', api.view_notification, name='view_notification'),
]
