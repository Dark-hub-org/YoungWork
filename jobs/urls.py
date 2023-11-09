from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('vacancies/', views.VacanciesDataView.as_view()),
    path('create-vacancy/', views.VacanciesCreateDataView.as_view()),
    path('vacancy-page/<int:pk>/', views.VacancyDetailView.as_view()),
    path('api/v1/events/', views.EventsDataView.as_view()),
]
