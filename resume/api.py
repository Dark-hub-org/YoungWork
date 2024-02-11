from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from .models import Resume
from .serializers import ResumeDataSerializer, ResumeDetailSerializer
from django.shortcuts import render


@api_view(['GET', 'DELETE'])
def resume_detail_data(pk):
    vacancy_detail = Resume.objects.get(pk=pk)
    serializer = ResumeDetailSerializer(vacancy_detail)
    return JsonResponse(serializer.data)


@api_view(['GET'])
def resume_of_users(pk):
    vacancy_detail = Resume.objects.filter(pk=pk)
    serializer = ResumeDataSerializer(vacancy_detail)
    return JsonResponse(serializer.data)


@api_view(['GET', 'POST'])
def resume_reg(request):
    serializer = ResumeDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return render(request, "index.html")
    return render(request, "index.html")
