from django.contrib import admin
from .models import *


@admin.register(Vacancies)
class VacanciesDisplay(admin.ModelAdmin):
    list_display = ["id", "job_title", "salary_min", "salary_max", "timestamp", "graph"]


@admin.register(Response)
class ResponseDisplay(admin.ModelAdmin):
    list_display = ["id", "date_start", "date_start", "result"]
