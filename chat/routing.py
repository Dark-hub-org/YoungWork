from django.urls import path, re_path

from . import consumers

websocket_urlpatterns = [
    path("ws/", consumers.ChatConsumer.as_asgi()),
    # path("ws/chat/", consumers.ChatConsumer.as_asgi()),
]
