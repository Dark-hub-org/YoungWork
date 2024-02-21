from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes

from accounts.forms import ProfileForm
from accounts.models import User
from accounts.serializers import UserAvatarSerializer


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
        'about': request.user.about,
        'aboutWork': request.user.about_work,
        'telegram': request.user.telegram,
        'website': request.user.website,
        'phoneNumber': request.user.phone_number,
    })


@api_view(['POST'])
def editpassword(request):
    user = request.user
    form = PasswordChangeForm(data=request.data, user=user)

    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'success'})
    else:
        return JsonResponse({'message': form.errors.as_json()}, safe=False)


@api_view(['POST'])
def upload_avatar(request):
    user = request.user

    form = ProfileForm(request.POST, request.FILES, instance=user)

    if form.is_valid():
        form.save()

    serializer = UserAvatarSerializer(user)

    return JsonResponse({'message': 'information updated', 'user': serializer.data})
