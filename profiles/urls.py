from django.urls import path
from .views import *
from . import api

urlpatterns = [
    path('applicant/<str:pk>/', ApplicantDetailView.as_view()),
    path('employer/<str:pk>/', EmployerDetailView.as_view()),
    # path('applicant/edit/<str:pk>/', EmployerDetailView.as_view()),
    # path('employer/edit/<str:pk>/', EmployerDetailView.as_view()),
    path('api/applicant/', api.create_applicant, name='applicant'),
    path('api/employer/', api.create_employer, name='employer'),
]
