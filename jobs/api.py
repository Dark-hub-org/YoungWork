from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Vacancies
from .serializers import VacanciesDetailSerializer


@api_view(['GET'])
def vacancy_data(request, pk):
    vacancy_detail = Vacancies.objects.get(pk=pk)
    serializer = VacanciesDetailSerializer(vacancy_detail)
    return JsonResponse(serializer.data)
