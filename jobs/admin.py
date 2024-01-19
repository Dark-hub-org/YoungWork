from django.contrib import admin
from .models import *


class Vacancy(admin.ModelAdmin):
    list_display = ["job_title", "salary_min", "salary_max", "timestamp"]


admin.site.register(Vacancies, Vacancy)
admin.site.register(Events)
