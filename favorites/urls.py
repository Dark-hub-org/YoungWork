from django.urls import path
from . import api

urlpatterns = [
    path('data-favorites/', api.favorites, name="favorites"),
    path('favorites-del/<str:pk>/', api.favorite_delete, name="delet_favorites"),
]
