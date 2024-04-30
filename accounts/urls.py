from django.urls import path
from . import api

urlpatterns = [
    path('me/', api.me, name='me'),
    path('user-data/<str:pk>/', api.user_data, name='user'),
    path('password-change/', api.editpassword, name='password_change'),
    path('upload-avatar/', api.upload_avatar, name='upload_avatar'),
    path('recommend/', api.recommend, name='recommend'),
    path('switch/', api.switch_profile, name='switch'),
    path('delete_photo/', api.delete_photo, name='delete_photo'),
    path('update_last_log_in/', api.update_last_login, name='update_last_login'),
]
