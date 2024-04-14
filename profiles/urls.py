from django.urls import path
from . import api

urlpatterns = [
    path('applicant/', api.applicant_view, name='applicant'),
    path('employer/', api.employer_view, name='employer'),
    path('applicant/edit/', api.edit_applicant_view, name='edit_applicant'),
    path('employer/edit/', api.edit_employer_view, name='edit_employer'),
    path('applicant/edit-data/<str:pk>/', api.edit_applicant, name='edit_applicant_data'),
    path('employer/edit-data/<str:pk>/', api.edit_employer, name='edit_employer_data'),
    path('applicant/data/<str:pk>/', api.applicant_data, name='data_applicant'),
    path('employer/data/<str:pk>/', api.employer_data, name='data_employer'),
    path('api/applicant/', api.create_applicant, name='create_applicant'),
    path('api/employer/', api.create_employer, name='create_employer'),
    path('api/applicant/upload-portfolio/', api.upload_portfolio, name='upload_portfolio'),
    path('api/employer/upload-photorg/', api.upload_photo_org, name='upload_photo_org'),
    path('api/employer/upload-achievements/', api.upload_achievements, name='upload_job_example'),
]
