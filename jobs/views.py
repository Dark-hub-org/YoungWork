from rest_framework.pagination import PageNumberPagination
from .models import Vacancies
from rest_framework import generics
from .serializers import VacanciesDataSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 9999


class VacanciesData(generics.ListAPIView):
    queryset = Vacancies.objects.filter(active=True).all()
    serializer_class = VacanciesDataSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]

    filterset_fields = {
        'salary_min': ["gt", "exact"], 'salary_max': ["lt", "exact"],
        "required_experience": ["exact"], 'employ': ["exact"],
    }
    search_fields = ['job_title', 'description', 'tasks', 'requirements', 'company_name']
