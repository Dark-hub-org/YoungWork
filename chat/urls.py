from django.urls import path

from . import api

urlpatterns = [
    path('can/', api.conversation_list, name='conversation_list'),
    path('<str:pk>/get-or-create/', api.conversation_get_or_create, name='conversation_get_or_create'),
    path('<str:pk>/send/', api.conversation_send_message, name='conversation_send_message'),
    path('<str:pk>/', api.conversation_detail, name='conversation_detail'),
]
