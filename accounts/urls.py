from django.urls import path
from . import api
from .views import *

urlpatterns = [
    path('me/', api.me, name='me'),
    path('applicant/<str:pk>/', ApplicantDetailView.as_view()),
    path('employer/<str:pk>/', EmployerDetailView.as_view()),
    # path('applicant/edit/<str:pk>/', views.EditApplicantView.as_view()),
    # path('employer/edit/<str:pk>/', views.EditEmployerView.as_view()),
    path('api/applicant/', api.create_applicant, name='applicant'),
    path('api/employer/', api.create_employer, name='employer'),
]
