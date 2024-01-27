from django.http import JsonResponse

from rest_framework.decorators import api_view

from accounts.models import User
from .serializers import ApplicantDataSerializer


@api_view(['POST'])
def create_profile(request):
    serializer = ApplicantDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors)
