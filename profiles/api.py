from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import CreateApplicantSerializer, CreateEmployerSerializer, EmployerDetailSerializer, \
    ApplicantDetailSerializer
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


@api_view(['GET', 'PATCH'])
def edit_employer(request, pk):
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
    title_org = request.data.get('titleOrg')
    photo_org = request.data.get('photoOrg')
    inn = request.data.get('inn')
    status_valid = request.data.get('statusValid')
    job_example = request.data.get('jobExample')
    user = User.objects.filter(pk=pk).update(first_name=first_name, last_name=last_name, surname=surname,
                                             date_of_birth=date_of_birth, citizenship=citizenship, region=region,
                                             city=city, about=about, about_work=about_work, telegram=telegram,
                                             website=website,
                                             phone_number=phone_number)
    serializer = UserSerializer(data=user)
    if serializer.is_valid():
        serializer.save()
    employer = Employer.objects.filter(pk=pk).update(title_org=title_org, photo_org=photo_org, inn=inn,
                                                     status_valid=status_valid, job_example=job_example)
    serializer = CreateEmployerSerializer(data=employer)
    if serializer.is_valid():
        serializer.save()
    return render(request, "index.html")


@api_view(['GET', 'PATCH'])
def edit_applicant(request, pk):
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
    portfolio = request.data.get('portfolio')
    user = User.objects.filter(pk=pk).update(first_name=first_name, last_name=last_name, surname=surname,
                                             date_of_birth=date_of_birth, citizenship=citizenship, region=region,
                                             city=city, about=about, about_work=about_work, telegram=telegram,
                                             website=website,
                                             phone_number=phone_number)
    serializer = UserSerializer(data=user)
    if serializer.is_valid():
        serializer.save()
    applicant = Applicant.objects.filter(pk=pk).update(portfolio=portfolio)
    serializer = CreateApplicantSerializer(data=applicant)
    if serializer.is_valid():
        serializer.save()
    return render(request, "index.html")


@api_view(['GET'])
def employer_view(request, pk):
    employer_detail = Employer.objects.get(pk=pk)
    serializer = EmployerDetailSerializer(employer_detail)
    return render(request, "index.html", serializer.data)


@api_view(['GET'])
def applicant_view(request, pk):
    applicant_detail = Applicant.objects.get(pk=pk)
    serializer = ApplicantDetailSerializer(applicant_detail)
    return render(request, "index.html", serializer.data)


@api_view(['GET'])
def employer_data(self, pk):
    employer_detail = Employer.objects.filter(pk=pk)
    serializer = EmployerDetailSerializer(employer_detail)
    return JsonResponse(serializer.data)


@api_view(['GET'])
def applicant_data(self, pk):
    applicant_detail = Applicant.objects.filter(pk=pk)
    serializer = ApplicantDetailSerializer(applicant_detail)
    return JsonResponse(serializer.data)
