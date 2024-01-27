from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import ProfileForm
from .models import User
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
def editprofile(request):
    user = request.user
    email = request.data.get('email')

    if User.objects.exclude(id=user.id).filter(email=email).exists():
        return JsonResponse({'message': 'email already exists'})
    else:
        form = ProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()

        serializer = UserSerializer(user)

        return JsonResponse({'message': 'information updated', 'user': serializer.data})


@api_view(['POST'])
def editpassword(request):
    user = request.user

    form = PasswordChangeForm(data=request.POST, user=user)

    if form.is_valid():
        form.save()

        return JsonResponse({'message': 'success'})
    else:
        return JsonResponse({'message': form.errors.as_json()}, safe=False)
