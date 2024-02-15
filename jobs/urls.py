from django.urls import path
from django.views.generic import TemplateView

from . import api
from .views import *

urlpatterns = [
    path('vacancy/', TemplateView.as_view(template_name='index.html')),
    path('api/vac/', VacanciesData.as_view()),
    path('vacancy/<str:pk>/', TemplateView.as_view(template_name='index.html')),
    path('api/vac/<str:pk>/', api.vacancy_detail_data, name="vacancy_data"),
    path('create-vacancy/', api.vacancy_reg, name="create_vacancy"),
    path('api/events/', EventsDataView.as_view()),
    path('api/active/vac/', api.active_vacancy, name="active_vac"),
    path('api/inactive/vac/', api.active_vacancy, name="inactive_vac"),
]
