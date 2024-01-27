from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('applicant/<str:pk>/', views.ApplicantDetailView.as_view()),
    path('employer/<str:pk>/', views.EmployerDetailView.as_view()),
    # path('applicant/edit/<str:pk>/', views.EmployerDetailView.as_view()),
    # path('employer/edit/<str:pk>/', views.EmployerDetailView.as_view()),
    path('api/applicant/', api.create_applicant, name='applicant'),
    path('api/employer/', api.create_employer, name='employer'),
]
