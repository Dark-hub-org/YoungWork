from django.urls import path
from . import views

urlpatterns = [
    path('create-resume/', views.SummaryDataView.as_view()),
    path('resumes/<int:pk>/', views.SummaryDetailView.as_view()),
]
