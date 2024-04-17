from rest_framework.pagination import PageNumberPagination
from .models import Vacancies
from rest_framework import generics
from .serializers import VacanciesDataSerializer
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 9999


class VacancyFilter(filters.FilterSet):
    min_salary = filters.NumberFilter(field_name="salary_min", lookup_expr='gte')
    employ = filters.CharFilter(lookup_expr='icontains')
    graph = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Vacancies
        fields = ['required_experience', ]


class VacanciesData(generics.ListAPIView):
    serializer_class = VacanciesDataSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    filterset_class = VacancyFilter
    search_fields = ['job_title', 'description', 'tasks', 'requirements', 'company_name']

    def get_queryset(self):
        user = self.request.user.id
        queryset = Vacancies.objects.filter(active=True).exclude(created_by=user)
        return queryset
