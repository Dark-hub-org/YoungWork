from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from accounts.models import User
from .models import Resume
from .serializers import ResumeDataSerializer, ResumeDetailSerializer
from django.shortcuts import render


@api_view(['GET', 'DELETE'])
def resume_detail_data(request, pk):
    resume_detail = Resume.objects.get(pk=pk)
    serializer = ResumeDetailSerializer(resume_detail)
    return JsonResponse(serializer.data)


@api_view(['GET'])
def resume_of_users(request, pk):
    resume_detail = Resume.objects.filter(pk=pk)
    serializer = ResumeDataSerializer(resume_detail)
    return JsonResponse(serializer.data)


@api_view(['GET', 'POST'])
def resume_reg(request):
    serializer = ResumeDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return render(request, "index.html")
    return render(request, "index.html")


@api_view(['GET'])
def ditail_data_of_user(request, pk):
    user = User.objects.get(pk=pk)
    return JsonResponse(data={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'surname': user.surname,
        'region': user.region,
        'citizenship': user.citizenship,
        'phone_number': user.phone_number,
    })
