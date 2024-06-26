from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from accounts.models import User
from .models import Vacancies
from .serializers import VacanciesDetailSerializer, VacanciesDataSerializer
from django.shortcuts import render


@api_view(['GET', 'POST'])
def vacancy_reg(request):
    serializer = VacanciesDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return render(request, "index.html")
    return render(request, "index.html")


@api_view(['PATCH'])
def edit_vacancy(request, pk):
    try:
        vacancy = Vacancies.objects.get(pk=pk)
    except Vacancies.DoesNotExist:
        return JsonResponse({'message': 'Vacancy not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = VacanciesDataSerializer(instance=vacancy, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def vacancy_detail_data(request, pk):
    try:
        vacancy_detail = Vacancies.objects.get(pk=pk)
    except Vacancies.DoesNotExist:
        return JsonResponse({'message': 'Vacancy not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = VacanciesDetailSerializer(vacancy_detail)
    return JsonResponse(serializer.data)


@api_view(['GET', 'POST'])
def active_vacancy(request):
    if request.method == 'POST':
        Vacancies.objects.filter(pk=request.data.get('pk')).update(active=True)
    active_vacancies = Vacancies.objects.filter(created_by=request.user.id, active=True)
    serializer = VacanciesDataSerializer(active_vacancies, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
def inactive_vacancy(request):
    if request.method == 'POST':
        Vacancies.objects.filter(pk=request.data.get('pk')).update(active=False)
    inactive_vacancies = Vacancies.objects.filter(created_by=request.user.id, active=False)
    serializer = VacanciesDataSerializer(inactive_vacancies, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def ditail_data_of_user(request, pk):
    user = User.objects.get(pk=pk)
    return JsonResponse(data={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'region': user.region,
        'citizenship': user.citizenship,
        'phone_number': user.phone_number,
    })


@api_view(['POST'])
def upload_preview(request):
    Vacancies.objects.filter(user=request.user.id).update(portfolio=request.data.get('portfolio'))
    return JsonResponse({'message': 'success'})


@api_view(['DELETE'])
def vacancy_delete(request, pk):
    vacancy = Vacancies.objects.filter(created_by=request.user.id).get(pk=pk)
    vacancy.delete()
    return JsonResponse({'message': 'vacancy deleted'})
