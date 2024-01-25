from django.urls import path
from . import api

urlpatterns = [
    path('me/', api.me, name='me'),
    path('editprofile/', api.editprofile, name='editprofile'),
    path('editpassword/', api.editpassword, name='editpassword'),
]
