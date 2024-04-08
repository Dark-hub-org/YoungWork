from django.contrib import admin
from .models import Favorites


@admin.register(Favorites)
class ResumeDisplay(admin.ModelAdmin):
    list_display = ["id", "timestamp"]
    search_fields = ["id", "timestamp"]
