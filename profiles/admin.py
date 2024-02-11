from django.contrib import admin
from .models import *


@admin.register(Applicant)
class ApplicantDisplay(admin.ModelAdmin):
    list_display = ["user", "portfolio"]


@admin.register(Employer)
class EmployerDisplay(admin.ModelAdmin):
    list_display = ["user", "inn", "title_org", "status_valid"]
