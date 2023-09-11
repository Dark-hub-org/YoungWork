from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import JsonResponse
from .models import Vacancy
from .serializer import VacancyListSerializer, VacancyDetailSerializer, VacancyCreateSerializer


class Site(APIView):
    def index(request):
        return render(request, "index.html")


class VacancyListView(APIView):

    def post(self, request):
        vacancy = Vacancy.objects.create(request.body)
        serializer = VacancyCreateSerializer(vacancy)
        return Response(serializer.data)

    def get(self, request):
        vacancy = Vacancy.objects.all()
        serializer = VacancyListSerializer(vacancy, many=True)
        return Response(serializer.data)


class VacancyDetailView(APIView):

    def get(self, request, pk):
        vacancy = Vacancy.objects.get(id=pk)
        serializer = VacancyDetailSerializer(vacancy)
        return Response(serializer.data)
