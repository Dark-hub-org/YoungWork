from rest_framework.pagination import PageNumberPagination
from .models import Resume
from rest_framework import generics
from .serializers import ResumeDataSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 9999


class ResumeData(generics.ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeDataSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]

    search_fields = []
    filterset_fields = []
