from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from .models import Vacancies
from .serializers import VacanciesDetailSerializer, VacanciesDataSerializer
from django.shortcuts import render


@api_view(['GET', 'DELETE'])
def vacancy_detail_data(request, pk):
    vacancy_detail = Vacancies.objects.get(pk=pk)
    serializer = VacanciesDetailSerializer(vacancy_detail)
    return JsonResponse(serializer.data)


# @api_view(['GET'])
# def vacancy_of_users(request):
#     vacancy_detail = Vacancies.objects.filter(created_by=request.user.id)
#     serializer = VacanciesDetailSerializer(vacancy_detail)
#     return JsonResponse(serializer.data)


@api_view(['GET', 'POST'])
def vacancy_reg(request):
    serializer = VacanciesDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return render(request, "index.html")
    return render(request, "index.html")


@api_view(['GET'])
def active_vacancy(request):
    active_vacancies = Vacancies.objects.filter(created_by=request.user.id, active=True)
    serializer = VacanciesDataSerializer(active_vacancies, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def inactive_vacancy(request):
    inactive_vacancies = Vacancies.objects.filter(created_by=request.user.id, active=False)
    serializer = VacanciesDataSerializer(inactive_vacancies)
    return JsonResponse(serializer.data, safe=False)

# @api_view(['DELETE'])
# def vacancy_delete(request, pk):
#     vacancy = Vacancies.objects.filter(created_by=request.user).get(pk=pk)
#     vacancy.delete()
#     return JsonResponse({'message': 'post deleted'})
