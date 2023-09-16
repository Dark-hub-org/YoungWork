from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('job-openings/', TemplateView.as_view(template_name='index.html')),
    path('create/', TemplateView.as_view(template_name='index.html')),
    path('api/v1/jobs_opening/', views.VacancyListView.as_view()),
    path('api/v1/jobs_opening/<int:pk>/', views.VacancyDetailView.as_view()),
]
