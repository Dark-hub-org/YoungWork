from django.urls import path
from . import api

urlpatterns = [
    path('applicant/<str:pk>/', api.applicant_view, name='applicant'),
    path('employer/<str:pk>/', api.employer_view, name='employer'),
    path('applicant/edit/<str:pk>/', api.edit_applicant_view, name='edit_applicant'),
    path('employer/edit/<str:pk>/', api.edit_employer_view, name='edit_employer'),
    path('applicant/edit-data/<str:pk>/', api.edit_applicant, name='edit_applicant_data'),
    path('employer/edit-data/<str:pk>/', api.edit_employer, name='edit_employer_data'),
    path('applicant/data/<str:pk>/', api.applicant_data, name='data_applicant'),
    path('applicant/data-more/<str:pk>/', api.applicant_data, name='data_applicant'),
    path('employer/data/<str:pk>/', api.employer_data, name='data_employer'),
    path('api/applicant/', api.create_applicant, name='create_applicant'),
    path('api/employer/', api.create_employer, name='create_employer'),
    # path('vacancy-response/<str:pk>/', api.response_on_vacancy, name='vacancy_response')
]
