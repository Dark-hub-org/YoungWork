from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Vacancies, Events
from rest_framework import generics
from .serializers import VacanciesDataSerializer, EventsDataSerializer, VacanciesDetailSerializer


class VacanciesDataView(APIView):
    def get(self, request):
        vacancies = Vacancies.objects.all()
        serializer = VacanciesDataSerializer(vacancies, many=True)
        return render(request, "index.html", {"vacancies": serializer.data})
#         return Response(serializer.data)


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class VacanciesData(generics.ListAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesDataSerializer
    pagination_class = LargeResultsSetPagination


class VacanciesCreateDataView(APIView):
    def post(self, request, format=None):
        serializer = VacanciesDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        return render(request, "index.html")


class VacancyDetailView(APIView):
    def get(self, request, pk):
        vacancy_detail = Vacancies.objects.get(pk=pk)
        serializer = VacanciesDetailSerializer(vacancy_detail)
        return render(request, "index.html", {'vacancy_detail': serializer.data})


class VacancyDetail(APIView):

    def get(self, request, pk):
        vacancy_detail = Vacancies.objects.get(pk=pk)
        serializer = VacanciesDetailSerializer(vacancy_detail)
        return Response(serializer.data)


class EventsDataView(APIView):
    def post(self, request, format=None):
        serializer = EventsDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        event = Events.objects.create(request.body)
        serializer = EventsDataSerializer(event)
        return render(request, "index.html", {"event": serializer})
