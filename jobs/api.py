from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from profiles.models import Applicant
from accounts.models import User
from .models import Vacancies, Response
from .serializers import VacanciesDetailSerializer, VacanciesDataSerializer, ResponseDataSerializer
from django.shortcuts import render
from notification.utils import create_notification


@api_view(['GET', 'POST'])
def vacancy_reg(request):
    serializer = VacanciesDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return render(request, "index.html")
    return render(request, "index.html")


# TODO: Test
@api_view(['PATCH'])
def edit_vacancy(request, pk):
    # vacancy_data = {
    #     "job_title": request.data.get('job_title'),
    #     "company_name": request.data.get('company_name'),
    #     "salary_min": request.data.get('salary_min'),
    #     "salary_max": request.data.get('salary_max'),
    #     "description": request.data.get('description'),
    #     "tasks": request.data.get('tasks'),
    #     "requirements": request.data.get('requirements'),
    #     "tax": request.data.get('tax'),
    #     "employ": request.data.get('employ'),
    #     "required_experience": request.data.get('required_experience'),
    #     "created_by": request.data.get('created_by'),
    #     "graph": request.data.get('graph'),
    # }
    # vacancy = Vacancies.objects.filter(pk=pk).update(**vacancy_data)
    # serializers = VacanciesDataSerializer(data=vacancy)
    # if serializers.is_valid():
    #     serializers.save()
    #     return JsonResponse(serializers.data)
    # return JsonResponse(serializers.data)
    try:
        vacancy = Vacancies.objects.get(pk=pk)
    except Vacancies.DoesNotExist:
        return JsonResponse({'message': 'Vacancy not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = VacanciesDataSerializer(instance=vacancy, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
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


@api_view(['POST'])
def response_on_vacancy(request):
    vacancy = request.data.get('vacancy')
    check = Response.objects.filter(created_by=request.user.id, vacancy=vacancy)

    if not check:
        serializer = ResponseDataSerializer(data=request.data)
        applicant_get = Applicant.objects.get(user=request.user.id)
        applicant_filter = Applicant.objects.filter(user=request.user.id)
        res = list(applicant_get.response.copy())
        res.append(vacancy)
        applicant_filter.update(response=res)
        if serializer.is_valid():
            serializer.save()
            notification = create_notification(request, 'new_vacancy_response', vacancy_id=vacancy)
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.data, safe=False)
    else:
        notification = create_notification(request, 'new_vacancy_response', vacancy_id=vacancy)
        return JsonResponse("Вы уже откликнулись", safe=False)


@api_view(['GET'])
def all_response(request):
    resp = Response.objects.filter(vacancy=request.data.get('pk'))
    serializer = ResponseDataSerializer(resp, many=True)
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

# @api_view(['DELETE'])
# def vacancy_delete(request, pk):
#     vacancy = Vacancies.objects.filter(created_by=request.user).get(pk=pk)
#     vacancy.delete()
#     return JsonResponse({'message': 'post deleted'})
