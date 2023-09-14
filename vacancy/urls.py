from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Site.index),
    path('api/v1/vacancys/', views.VacancyListView.as_view()),
    path('api/v1/vacancy/<int:pk>/', views.VacancyDetailView.as_view()),
]
