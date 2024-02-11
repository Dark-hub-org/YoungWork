from django.contrib import admin
from .models import *


@admin.register(Vacancies)
class VacanciesDisplay(admin.ModelAdmin):
    list_display = ["id", "job_title", "salary_min", "salary_max", "timestamp", "graph"]


@admin.register(Events)
class EventsDisplay(admin.ModelAdmin):
    list_display = ["id", "event_type", "date_start", "date_start", "result"]
