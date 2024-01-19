from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/auth/users/', MyUserDataView.as_view()),
]
