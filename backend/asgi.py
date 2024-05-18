import os
import django
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter

from django.core.asgi import get_asgi_application
from chat.middleware import JwtAuthMiddlewareStack
from chat import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.prod')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": JwtAuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
