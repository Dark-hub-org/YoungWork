from django.contrib import admin
from .models import *


class Applic(admin.ModelAdmin):
    list_display = ["user", "bio"]


class Employ(admin.ModelAdmin):
    list_display = ["user", "inn", "title_org", "job_title", "status_validatio"]


admin.site.register(Applicant, Applic)
admin.site.register(Employer, Employ)
