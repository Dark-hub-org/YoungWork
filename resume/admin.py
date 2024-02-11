from django.contrib import admin
from .models import *


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ["id", "resume_title", "employ", "about_us", "experience"]


@admin.register(Favorites)
class FavoritesDisplay(admin.ModelAdmin):
    list_display = ["id", "created_by", "timestamp"]
