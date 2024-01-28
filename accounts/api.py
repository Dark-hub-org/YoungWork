from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes


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
