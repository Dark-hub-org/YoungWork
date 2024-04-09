from django.contrib import admin
from .models import *


@admin.register(Vacancies)
class VacanciesDisplay(admin.ModelAdmin):
    list_display = ["job_title", "salary_min", "salary_max", "timestamp", "graph"]
    list_filter = ["timestamp"]
    search_fields = ["id", "job_title", "graph"]
