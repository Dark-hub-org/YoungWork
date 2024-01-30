from django.urls import path
from . import api
from .views import *

urlpatterns = [
    path('vacancy/', VacanciesDataView.as_view()),
    path('api/vac/', VacanciesData.as_view()),
    path('vacancy/<str:pk>/', VacancyDetailView.as_view()),
    path('api/vac/<str:pk>/', api.vacancy_detail_data, name="vacancy_data"),
    path('create-vacancy/', api.vacancy_regstr, name="create_vacancy"),
    path('api/events/', EventsDataView.as_view()),
]
