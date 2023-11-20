from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/damp', views.DRFDampUserDataView.as_view()),
    path('api/v1/damp/<int:pk>/', views.DRFDampUserDetailView.as_view())
]
