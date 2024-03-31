from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from .models import Resume
from jobs.models import Vacancies
from .serializers import ResumeDataSerializer, ResumeDetailSerializer
from django.shortcuts import render
from .models import Favorites
from jobs.serializers import VacanciesDataSerializer
from django.core.exceptions import ObjectDoesNotExist
from notification.utils import create_notification


@permission_classes([IsAuthenticated])
@api_view(['GET', 'DELETE'])
def resume_detail_data(request, pk):
    resume_detail = Resume.objects.get(pk=pk)
    serializer = ResumeDetailSerializer(resume_detail)
    return JsonResponse(serializer.data)


@api_view(['GET'])
def resume_of_users(request):
    resume = Resume.objects.filter(created_by=request.user.id)
    serializer = ResumeDataSerializer(resume)
    return JsonResponse(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def resume_reg(request):
    serializer = ResumeDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return render(request, "index.html")
    return render(request, "index.html")


@permission_classes([IsAuthenticated])
@api_view(['POST', 'GET'])
def favorites(request):
    user = request.user
    if request.method == 'POST':
        if Favorites.objects.filter(created_by=user).exists():
            instance = Favorites.objects.get(created_by=user)
            instance.vacancy.add(request.data.get('vacancy'))
            notification = create_notification(request, 'vacancy_favorites')
            return JsonResponse({'message': 'add success'})
        else:
            instance = Favorites.objects.create(created_by=user)
            instance.vacancy.set([request.data.get('vacancy')])
            return JsonResponse({'message': 'success'})
    elif Favorites.objects.filter(created_by=user).exists():
        instance = Favorites.objects.get(created_by=user)
        fav_vac = instance.vacancy.all()
        serializer = VacanciesDataSerializer(fav_vac, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'message': 'empty_space'})


@api_view(['DELETE'])
def favorite_delete(request, pk):
    user = request.user
    try:
        fav = Favorites.objects.get(created_by=user)
        vacancy = Vacancies.objects.get(pk=pk)
        fav.vacancy.remove(vacancy)
        return JsonResponse({'message': 'Vacancy removed from favorites'})
    except ObjectDoesNotExist:
        return JsonResponse({'message': 'Favorites not found'}, status=404)
    except Vacancies.DoesNotExist:
        return JsonResponse({'message': 'Vacancy not found'}, status=404)


@permission_classes([IsAuthenticated])
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
