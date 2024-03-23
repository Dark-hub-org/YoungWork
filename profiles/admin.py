from django.contrib import admin
from .models import *


@admin.register(Applicant)
class ApplicantDisplay(admin.ModelAdmin):
    list_display = ["user", "portfolio"]
    search_fields = ["user"]


@admin.register(Employer)
class EmployerDisplay(admin.ModelAdmin):
    list_display = ["user", "title_org", "inn", "status_valid"]
    list_filter = ["status_valid"]
    search_fields = ["user", "title_org"]
