from django.urls import include, path
from rest_framework import routers
from .views import YourModelViewSet

router = routers.DefaultRouter()
router.register(r'yourmodels', YourModelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
