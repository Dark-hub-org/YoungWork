from django.urls import path
from .views import *
from . import api

urlpatterns = [
    path('applicant/<str:pk>/', ApplicantDetailView.as_view()),
    path('employer/<str:pk>/', EmployerDetailView.as_view()),
    path('applicant/edit/<str:pk>/', api.edit_applicant, name='edit_applicant'),
    path('employer/edit/<str:pk>/', api.edit_employer, name='edit_employer'),
    path('api/applicant/', api.create_applicant, name='create_applicant'),
    path('api/employer/', api.create_employer, name='create_Яemployer'),
]
