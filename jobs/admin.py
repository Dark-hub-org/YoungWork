from django.contrib import admin
from .models import *


@admin.register(Vacancies)
class Vacancyies_Admin(admin.ModelAdmin):
    list_display = ["id", "job_title", "salary_min", "salary_max", "timestamp", "graph"]


@admin.register(Events)
class Event_Admin(admin.ModelAdmin):
    list_display = ["id", "event_type", "date_start", "date_start", "result"]
