from jobs.models import Vacancies
from resume.models import Resume
from jobs.serializers import VacanciesDataSerializer
from resume.serializers import ResumeDataSerializer
from notification.utils import create_notification
from .models import Favorites
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


@permission_classes([IsAuthenticated])
@api_view(['POST', 'GET'])
def favorites(request):
    user = request.user
    user_type = request.user.usertype
    if user_type == "employer":
        if request.method == 'POST':
            resume = request.data.get('resume')
            if Favorites.objects.filter(created_by=user).exists():
                instance = Favorites.objects.get(created_by=user)
                instance.resume.add(request.data.get('resume'))
                create_notification(request, 'resume_favorites', resume_id=resume)
                return JsonResponse({'message': 'add success'})
            else:
                instance = Favorites.objects.create(created_by=user)
                instance.resume.set([request.data.get('resume')])
                return JsonResponse({'message': 'create success'})
        elif Favorites.objects.filter(created_by=user).exists():
            instance = Favorites.objects.get(created_by=user)
            fav_res = instance.resume.all()
            serializer = ResumeDataSerializer(fav_res, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'message': 'empty_space'})
    else:
        vacancy = request.data.get('vacancy')
        if request.method == 'POST':
            if Favorites.objects.filter(created_by=user).exists():
                instance = Favorites.objects.get(created_by=user)
                instance.vacancy.add(request.data.get('vacancy'))
                create_notification(request, 'vacancy_favorites', vacancy_id=vacancy)
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
    user_type = request.user.usertype
    if user_type == "employer":
        try:
            fav = Favorites.objects.get(created_by=user)
            resume = Resume.objects.get(pk=pk)
            fav.resume.remove(resume)
            return JsonResponse({'message': 'Resume removed from favorites'})
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Favorites not found'}, status=404)
        except Resume.DoesNotExist:
            return JsonResponse({'message': 'Resume not found'}, status=404)
    else:
        try:
            fav = Favorites.objects.get(created_by=user)
            vacancy = Vacancies.objects.get(pk=pk)
            fav.vacancy.remove(vacancy)
            return JsonResponse({'message': 'Vacancy removed from favorites'})
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Favorites not found'}, status=404)
        except Vacancies.DoesNotExist:
            return JsonResponse({'message': 'Vacancy not found'}, status=404)
