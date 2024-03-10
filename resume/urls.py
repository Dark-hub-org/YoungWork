from django.urls import path
from django.views.generic import TemplateView

from . import api
from .views import *

urlpatterns = [
    path('resume/', TemplateView.as_view(template_name='index.html')),
    path('api/res/', ResumeData.as_view()),
    path('resume/<str:pk>/', TemplateView.as_view(template_name='index.html')),
    path('api/res/<str:pk>/', api.resume_detail_data, name="vacancy_ditail_data"),
    path('api/res/user/', api.resume_of_users, name="user_of_resume"),
    path('create-resume/', api.resume_reg, name="create_resume"),
#     path('favorites/', TemplateView.as_view(template_name='index.html')),
    path('favorites/', api.favorites, name="favorites"),
]
