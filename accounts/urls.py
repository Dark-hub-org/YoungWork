from django.urls import path
from . import api

urlpatterns = [
    path('me/', api.me, name='me'),
    path('password-change/', api.editpassword, name='password_change'),
    path('upload-avatar/', api.upload_avatar, name='upload_avatar'),
]
