from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import ProfileForm
from .models import Applicant
from .serializers import UserSerializer


@api_view(['GET'])
def me(request):
    data = {
        'id': request.user.id,
        'first_name': request.user.first_name,
        'email': request.user.email,
        'usertype': request.user.usertype,
        'last_name': request.user.last_name,
        'surname': request.user.surname,
        'date_of_birth': request.user.date_of_birth,
        'citizenship': request.user.citizenship,
        'region': request.user.region,
        'city': request.user.city,
        'avatar': request.user.get_avatar()
    }
    return JsonResponse(data)


@api_view(['POST'])
def create_applicant(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors)


@api_view(['POST'])
def create_employer(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors)
