from django.urls import path
from . import api

urlpatterns = [
    path('api/all-response/<str:pk>/', api.all_response, name="response_org"),
    path('api/response/', api.response_on_vacancy, name="response_on_vacancy"),
    path('api/accept/', api.accepted, name="accept")
]
