from django.urls import path
from .views import *

urlpatterns = [
    path('create-resume/', SummaryDataView.as_view()),
    path('resumes/<int:pk>/', SummaryDetailView.as_view()),
]
