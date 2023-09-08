from django.urls import path

from . import views

urlpatterns = [
    path("vacancy/", views.VacancyListView.as_view()),
]
