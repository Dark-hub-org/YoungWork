from django.urls import path
from . import views

urlpatterns = [
    path('profile/applicant/<int:pk>/', views.ApplicantDetailView.as_view()),
    path('profile/employer/<int:pk>/', views.EmployerDetailView.as_view()),
    path('api/v1/applicant/', views.DRFApplicantDataView.as_view()),
    path('api/v1/applicant/<int:pk>/', views.DRFApplicantDetailView.as_view()),
    path('api/v1/employer/', views.DRFEmployerDataView.as_view()),
    path('api/v1/employer/<int:pk>/', views.DRFEmployerDetailView.as_view()),
]
