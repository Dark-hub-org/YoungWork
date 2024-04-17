from django.contrib import admin
from .models import *


@admin.register(Response)
class ResponseDisplay(admin.ModelAdmin):
    list_display = ["id", "result", "date_start", "data_end"]
    list_filter = ["result"]
    search_fields = ["id", "date_start", "data_end", "result"]
