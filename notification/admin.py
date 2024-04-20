from django.contrib import admin

from .models import Notification


@admin.register(Notification)
class VacanciesDisplay(admin.ModelAdmin):
    list_display = ["id", "type_of_notification", "resume", "vacancy", "vacancyresponse", "created_by", "created_for"]
    list_filter = ["type_of_notification"]
    search_fields = ["id"]
