from django.urls import path
from . import api

urlpatterns = [
    path('applicant/<str:pk>/', api.applicant_view, name='applicant'),
    path('employer/<str:pk>/', api.employer_view, name='employer'),
    path('applicant/edit/<str:pk>/', api.edit_applicant, name='edit_applicant'),
    path('employer/edit/<str:pk>/', api.edit_employer, name='edit_employer'),
    path('api/applicant/', api.create_applicant, name='create_applicant'),
    path('api/employer/', api.create_employer, name='create_Яemployer'),
]
