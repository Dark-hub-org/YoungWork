from django.urls import path
from .views import *

urlpatterns = [
    path('vacancies/', VacanciesDataView.as_view()),
    path('api/v1/vac', VacanciesData.as_view()),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view()),
    path('create-vacancy/', VacanciesCreateDataView.as_view()),
    path('api/v1/events/', EventsDataView.as_view()),
]
