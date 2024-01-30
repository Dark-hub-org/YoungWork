from django.urls import path
from . import api

urlpatterns = [
    path('me/', api.me, name='me'),
]
