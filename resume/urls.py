from django.urls import path
from django.views.generic import TemplateView

from . import api
from .views import *

urlpatterns = [
    path('resume/', TemplateView.as_view(template_name='index.html')),
    path('api/res/', ResumeData.as_view()),
    path('resume/<str:pk>/', TemplateView.as_view(template_name='index.html')),
    path('favorites/', TemplateView.as_view(template_name='index.html')),
    path('api/active/res/', api.activate_resume, name="active_res"),
    path('api/inactive/res/', api.inactivate_resume, name="inactive_res"),
    path('api/res/<str:pk>/', api.resume_detail_data, name="vacancy_ditail_data"),
    path('api/resume/user/', api.resume_of_users, name="user_of_resume"),
    path('create-resume/', api.resume_reg, name="create_resume"),
    path('edit-resume/<str:pk>/', TemplateView.as_view(template_name='index.html')),
    path('api/edit-resume/<str:pk>/', api.edit_resume, name="edit_vacancy"),
    path('api/resume/delete/<str:pk>/', api.resume_delete, name="del_resume"),
]
