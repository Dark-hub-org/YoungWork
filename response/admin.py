from django.contrib import admin
from .models import *


@admin.register(Response)
class ResponseDisplay(admin.ModelAdmin):
    list_display = ["id", "date_start", "data_end", "result"]
    search_fields = ["id", "date_start", "data_end", "result"]
