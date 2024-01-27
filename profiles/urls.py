from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('profile/applicant/<str:pk>/', views.ApplicantDetailView.as_view()),
    path('profile/employer/<str:pk>/', views.EmployerDetailView.as_view()),
    path('profile/edit/<str:pk>/', views.EmployerDetailView.as_view()),
    path('api/applicant/', api.create_profile, name='applicant'),
    path('api/employer/', api.create_profile, name='employer'),
]
