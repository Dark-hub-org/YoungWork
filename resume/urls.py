from django.urls import path
from django.views.generic import TemplateView

from . import api
from .views import *

urlpatterns = [
    path('create-resume/', api.resume_reg, name="create_resume"),
    path('resume/', ResumeData.as_view()),
    path('resume/<str:pk>/', TemplateView.as_view(template_name='index.html')),
    path('api/res/<str:pk>/', api.resume_detail_data, name="vacancy_ditail_data"),
    path('detail-data/<str:pk>/', api.ditail_data_of_user, name='ditail-data'),
]
