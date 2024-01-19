from django.contrib import admin
from .models import *


class Resume(admin.ModelAdmin):
    list_display = ["summary_title", "type", "about_us", "experience"]


admin.site.register(Summary, Resume)
