from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('create-resume/', TemplateView.as_view(template_name='index.html')),
    path('api/v1/resumes/', views.SummaryDataView.as_view()),
    path('api/v1/resumes/<int:pk>/', views.SummaryDetailView.as_view()),
    path('api/v1/create-resume/', views.SummaryDataView.as_view()),
]
