from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import CreateApplicantSerializer, CreateEmployerSerializer, EmployerDetailSerializer, \
    ApplicantDetailSerializer, EmployerDataSerializer, ApplicantDataSerializer
from .models import Employer, Applicant
from accounts.models import User
from accounts.serializers import UserSerializer
from django.shortcuts import render


def edit_user_data(request, pk):
    first_name = request.data.get('firstName')
    last_name = request.data.get('lastName')
    surname = request.data.get('surname')
    date_of_birth = request.data.get('dateOfBirth')
    citizenship = request.data.get('citizenship')
    region = request.data.get('region')
    city = request.data.get('city')
    about = request.data.get('about')
    about_work = request.data.get('aboutWork')
    telegram = request.data.get('telegram')
    website = request.data.get('website')
    phone_number = request.data.get('phoneNumber')

    user = User.objects.filter(pk=pk).update(
        first_name=first_name, last_name=last_name, surname=surname,
        date_of_birth=date_of_birth, citizenship=citizenship, region=region,
        city=city, about=about, about_work=about_work, telegram=telegram, website=website,
        phone_number=phone_number
    )
    serializers = UserSerializer(data=user)
    if serializers.is_valid():
        serializers.save()
        return JsonResponse(serializers.data)
    return JsonResponse(serializers.data)


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


@api_view(['GET'])
def edit_applicant_view(request, pk):
    return render(request, "index.html")


@api_view(['GET'])
def edit_employer_view(request, pk):
    return render(request, "index.html")


@api_view(['PATCH'])
def edit_employer(request, pk):
    title_org = request.data.get('title_org')
    # photo_org = request.data.get('photo_org')
    inn = request.data.get('inn')
    status_valid = request.data.get('status_valid')
    # job_example = request.data.get('job_example')

    edit_user_data(request, pk)
    employer = Employer.objects.filter(pk=pk).update(title_org=title_org, status_valid=status_valid, inn=inn)
    serializer = EmployerDataSerializer(data=employer)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.data)


@api_view(['PATCH'])
def edit_applicant(request, pk):
    portfolio = request.data.get('portfolio')

    edit_user_data(request, pk)
    applicant = Applicant.objects.filter(pk=pk).update(portfolio=portfolio)
    serializer = ApplicantDataSerializer(data=applicant)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.data)


@api_view(['GET'])
def employer_view(request, pk):
    return render(request, "index.html")


@api_view(['GET'])
def applicant_view(request, pk):
    return render(request, "index.html")


@api_view(['GET'])
def employer_data(self, pk):
    employer_detail = Employer.objects.get(pk=pk)
    serializer = EmployerDetailSerializer(employer_detail)
    return JsonResponse(serializer.data)


@api_view(['GET'])
def applicant_data(self, pk):
    applicant_detail = Applicant.objects.get(pk=pk)
    serializer = ApplicantDetailSerializer(applicant_detail)
    return JsonResponse(serializer.data)
