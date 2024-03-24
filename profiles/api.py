from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from .serializers import CreateApplicantSerializer, CreateEmployerSerializer, EmployerDetailSerializer, \
    ApplicantDetailSerializer, EmployerDataSerializer, ApplicantDataSerializer
from .models import Employer, Applicant
from accounts.models import User, VacancyResponse
from accounts.serializers import EditProfileSerializer
from django.shortcuts import render
from notification.utils import create_notification
from rest_framework.permissions import IsAuthenticated
from django.core.files.base import ContentFile


def edit_user_data(request):
    user_data = {
        "first_name": request.data.get('firstName'),
        "last_name": request.data.get('lastName'),
        "surname": request.data.get('surname'),
        "date_of_birth": request.data.get('dateOfBirth'),
        "citizenship": request.data.get('citizenship'),
        "region": request.data.get('region'),
        "city": request.data.get('city'),
        "about": request.data.get('about'),
        "about_work": request.data.get('aboutWork'),
        "telegram": request.data.get('telegram'),
        "website": request.data.get('website'),
        "phone_number": request.data.get('phoneNumber'),
    }
    user = User.objects.filter(pk=request.user.id).update(**user_data)
    serializers = EditProfileSerializer(data=user)
    if serializers.is_valid():
        serializers.save()
        return JsonResponse(serializers.data)
    return JsonResponse(serializers.data)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_applicant(request):
    serializer = CreateApplicantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_employer(request):
    serializer = CreateEmployerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def edit_applicant_view(request):
    return render(request, "index.html")


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def edit_employer_view(request):
    return render(request, "index.html")


@permission_classes([IsAuthenticated])
@api_view(['PATCH'])
def edit_employer(request, pk):
    employer_data = {
        "title_org": request.data.get('title_org'),
        "photo_org": request.data.get('photo_org'),
        "inn": request.data.get('inn'),
        "status_valid": request.data.get('status_valid'),
        "job_example": request.data.get('job_example'),
    }

    edit_user_data(request)
    employer = Employer.objects.filter(pk=pk).update(**employer_data)
    serializer = EmployerDataSerializer(data=employer)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['PATCH'])
def edit_applicant(request, pk):
    portfolio = request.data.get('portfolio')

    edit_user_data(request)
    applicant = Applicant.objects.filter(pk=pk).update(portfolio=portfolio)
    serializer = ApplicantDataSerializer(data=applicant)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.data)


@api_view(['GET'])
def employer_view(request):
    return render(request, "index.html")


@api_view(['GET'])
def applicant_view(request):
    return render(request, "index.html")


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def employer_data(self, pk):
    employer_detail = Employer.objects.get(pk=pk)
    serializer = EmployerDetailSerializer(employer_detail)
    return JsonResponse(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def applicant_data(self, pk):
    applicant_detail = Applicant.objects.get(pk=pk)
    serializer = ApplicantDetailSerializer(applicant_detail)
    return JsonResponse(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def upload_portfolio(request):
    Applicant.objects.filter(user=request.data.get('pk')).update(portfolio=request.data.get('portfolio'))
    return JsonResponse({'message': 'success'})


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def upload_photo_org(request):
    employer = Employer.objects.filter(user=request.data.get('pk')).get()
    if 'photo_org' in request.FILES:
        photo_org_file = request.FILES['photo_org']
        photo_name = f"org_{employer.user.id}_photo.jpg"
        employer.photo_org.save(photo_name, ContentFile(photo_org_file.read()), save=True)
        return JsonResponse({'message': 'success'})
    else:
        return JsonResponse({'message': 'no avatar provided'}, status=400)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def upload_job_example(request):
    example = Employer.objects.filter(user=request.data.get('pk')).update(job_example=request.data.get('job_example'))
    return JsonResponse({'user': example})


@api_view(['GET'])
def response_on_vacancy(request, pk):
    user = User.objects.get(pk=pk)

    check_one = VacancyResponse.objects.filter(created_for=request.user).filter(created_by=user)
    check_two = VacancyResponse.objects.filter(created_for=user).filter(created_by=request.user)

    if not check_one or not check_two:
        vacancy_response = VacancyResponse.objects.create(created_for=user, created_by=request.user)

        notification = create_notification(request, 'new_vacancy_response', vacancy_response_id=vacancy_response.id)

        return JsonResponse({'message': 'Response on vacancy, success'})
    else:
        return JsonResponse({'message': 'Error'})
