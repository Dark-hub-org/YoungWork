from django.contrib import admin
from .models import *


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ["resume_title", "employ", "about_us", "experience"]
    list_filter = ["timestamp"]
    search_fields = ["id", "resume_title"]
