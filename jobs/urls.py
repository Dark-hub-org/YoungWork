from django.urls import path
from . import views

urlpatterns = [
    path('vacancies/', views.VacanciesDataView.as_view()),
    path('api/v1/vac', views.VacanciesData.as_view()),
    path('vacancies/<int:pk>/', views.VacancyDetailView.as_view()),
    path('create-vacancy/', views.VacanciesCreateDataView.as_view()),
    path('api/v1/events/', views.EventsDataView.as_view()),
]
