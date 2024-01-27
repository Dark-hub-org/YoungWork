from django.contrib import admin
from .models import *


class Resume(admin.ModelAdmin):
    list_display = ["summary_title", "type", "about_us", "experience"]


class Fav(admin.ModelAdmin):
    list_display = ["id", "created_by", "created_at"]


admin.site.register(Summary, Resume)
admin.site.register(Favorites, Fav)
