from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import JsonResponse
from .models import Vacancy
from .serializer import VacancyListSerializer


class Site(APIView):
    def index(request):
        return render(request, "index.html")


class VacancyListView(APIView):

    def get(self, request):
        vacancy = Vacancy.objects.all()
        serializer = VacancyListSerializer(vacancy, many=True)
        return render(request, "index.html", {"vacancy": serializer})
