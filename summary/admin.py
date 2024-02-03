from django.contrib import admin
from .models import *


@admin.register(Summary)
class Resume(admin.ModelAdmin):
    list_display = ["summary_title", "type", "about_us", "experience"]


@admin.register(Favorites)
class Fav(admin.ModelAdmin):
    list_display = ["id", "created_by", "created_at"]
