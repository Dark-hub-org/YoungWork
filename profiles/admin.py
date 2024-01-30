from django.contrib import admin
from .models import *


class Applic(admin.ModelAdmin):
    list_display = ["user", "portfolio"]


class Employ(admin.ModelAdmin):
    list_display = ["user", "inn", "title_org", "status_valid"]


admin.site.register(Applicant, Applic)
admin.site.register(Employer, Employ)
