from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import CreateApplicantSerializer, CreateEmployerSerializer
from .models import Employer, Applicant
from accounts.models import User
from accounts.serializers import UserSerializer
from django.shortcuts import render


@api_view(['POST'])
def create_applicant(request):
    serializer = CreateApplicantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors)


@api_view(['POST'])
def create_employer(request):
    serializer = CreateEmployerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors)


@api_view(['GET', 'UPDATE'])
def edit_employer(request, pk):
    user = User.objects.filter(pk=pk).update(first_name=request.data)
    serializer = UserSerializer(data=user)
    if serializer.is_valid():
        serializer.save()
    employer = Employer.objects.filter(pk=pk).update(job_title=request.data)
    serializer = CreateEmployerSerializer(data=employer)
    if serializer.is_valid():
        serializer.save()
    return render(request, "index.html")


@api_view(['GET', 'UPDATE'])
def edit_applicant(request, pk):
    user = User.objects.filter(id=pk).update(request.data)
    serializer = UserSerializer(user)
    if serializer.is_valid():
        serializer.save()
    applicant = Applicant.objects.filter(id=pk).update(request.data)
    serializer = CreateApplicantSerializer(applicant)
    if serializer.is_valid():
        serializer.save()
    return render(request, "index.html")
