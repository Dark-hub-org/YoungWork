from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes


@api_view(['GET'])
def me(request):
    return JsonResponse(data={
        'id': request.user.id,
        'firstName': request.user.first_name,
        'email': request.user.email,
        'usertype': request.user.usertype,
        'lastName': request.user.last_name,
        'surname': request.user.surname,
        'dateOfBirth': request.user.date_of_birth,
        'citizenship': request.user.citizenship,
        'region': request.user.region,
        'city': request.user.city,
        'avatar': request.user.get_avatar(),
        'about': request.user.about,
        'aboutWork': request.user.about_work,
        'telegram': request.user.telegram,
        'website': request.user.website,
        'phoneNumber': request.user.phone_number,
    })
