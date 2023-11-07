from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('vacancies/', TemplateView.as_view(template_name='index.html')),
    path('create-vacancy', TemplateView.as_view(template_name='index.html')),
    path('vacancy-page/<int:pk>/', TemplateView.as_view(template_name='index.html')),
    path('api/v1/vacancies/', views.VacanciesDataView.as_view()),
    path('api/v1/vacancies/', views.VacanciesDataView.as_view()),
    path('api/v1/vacancies/<int:pk>/', views.VacancyDetailView.as_view()),
    path('api/v1/events/', views.EventsDataView.as_view()),
]
