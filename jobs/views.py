from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import Vacancies, Events
from rest_framework import generics
from .serializers import VacanciesDataSerializer, EventsDataSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 9999


class VacanciesData(generics.ListAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesDataSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

    filterset_fields = ['salary_min', 'required_experience', 'type', ]
    search_fields = ['job_title', 'description', 'tasks', 'requirements']


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
