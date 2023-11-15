from django.urls import path
from . import views

urlpatterns = [
    path('create-resume/', views.SummaryDataView.as_view()),
    path('api/v1/create-resume/', views.SummaryDataView.as_view()),
    path('api/v1/resumes/', views.DRFSummaryDataView.as_view()),
    path('api/v1/resumes/<int:pk>/', views.DRFSummaryDetailView.as_view()),
    path('api/v1/create-resume/', views.DRFSummaryDataView.as_view()),
]
