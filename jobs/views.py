from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Vacancies, Events
from rest_framework import generics
from .serializers import VacanciesDataSerializer, EventsDataSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 9999


class VacanciesData(generics.ListAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesDataSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]

    filterset_fields = {
        'salary_min': ["gt", "exact"], 'salary_max': ["lt", "exact"],
        "required_experience": ["exact"], 'employ': ["exact"],
    }
    search_fields = ['job_title', 'description', 'tasks', 'requirements', 'company_name']


class EventsDataView(APIView):
    def post(self, request):
        serializer = EventsDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        event = Events.objects.create(request.body)
        serializer = EventsDataSerializer(event)
        return render(request, "index.html", {"event": serializer})
