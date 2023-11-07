from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('profile/applicant/', TemplateView.as_view(template_name='index.html')),
    path('profile/employer/', TemplateView.as_view(template_name='index.html')),
    path('api/v1/applicant/<int:pk>/', views.ApplicantDetailView.as_view()),
    path('api/v1/employer/', views.EmployerDataView.as_view()),
]
