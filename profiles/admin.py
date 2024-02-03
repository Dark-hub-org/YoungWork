from django.contrib import admin
from .models import *


@admin.register(Applicant)
class Applic(admin.ModelAdmin):
    list_display = ["user", "portfolio"]


@admin.register(Employer)
class Employ(admin.ModelAdmin):
    list_display = ["user", "inn", "title_org", "status_valid"]
