from django.contrib import admin
from .models import *


class Vacancy(admin.ModelAdmin):
    list_display = ["id", "job_title", "salary_min", "salary_max", "timestamp", "graph"]


class Event(admin.ModelAdmin):
    list_display = ["id", "event_type", "date_start", "date_start", "result"]


admin.site.register(Vacancies, Vacancy)
admin.site.register(Events, Event)
