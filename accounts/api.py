from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from backend.settings import *

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from profiles.models import Applicant, Employer
from jobs.models import Vacancies
from resume.models import Resume
from jobs.serializers import VacanciesDataSerializer
from django.core.files.base import ContentFile
from .serializers import UserFromSerializer


@permission_classes([IsAuthenticated])
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
        'avatar': request.user.get_avatar(),
        'region': request.user.region,
        'city': request.user.city,
        'about': request.user.about,
        'aboutWork': request.user.about_work,
        'telegram': request.user.telegram,
        'website': request.user.website,
        'phoneNumber': request.user.phone_number,
    })


@api_view(['GET'])
def user_data(request, pk):
    user_data = User.objects.filter(pk=pk).get()
    serializer = UserFromSerializer(user_data)
    return JsonResponse(serializer.data, safe=False)


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
    email = request.data.get('email')
    user = User.objects.filter(email=email).get()
    if request.data.get('avatar') == 1:
        instance = User.objects.get(email=email)
        instance.avatar = None
        instance.save()
        return JsonResponse({'message': 'success'})
    else:
        if 'avatar' in request.FILES:
            avatar_file = request.FILES['avatar']
            photo_name = f"{user.id}"
            user.avatar.save(photo_name, ContentFile(avatar_file.read()), save=True)
            return JsonResponse({'message': 'success'})
        else:
            return JsonResponse({'message': 'no avatar provided'}, status=400)


@api_view(['POST'])
def delete_photo(request):
    try:
        file_path = request.data.get('file_path')
        if os.path.exists(BASE_DIR + '/frontend/dist' + file_path):
            os.remove(BASE_DIR + '/frontend/dist' + file_path)
            return Response({'message': 'File deleted successfully'})
        else:
            return Response({'message': 'File does not exist'}, status=404)
    except Exception as e:
        return Response({'message': str(e)}, status=500)


@api_view(['POST'])
def switch_profile(request):
    user = request.user
    if user.usertype == 'applicant':
        profile_model = Applicant
        new_type = 'employer'
    else:
        profile_model = Employer
        new_type = 'applicant'

    if not profile_model.objects.filter(user=user).exists():
        profile_model.objects.create(user=user)

    User.objects.filter(id=user.id).update(usertype=new_type)
    return JsonResponse({'message': f'switch on {new_type}'})


@api_view(['GET'])
def recommend(request):
    user = request.user.id
    vac = Vacancies.objects.all()
    if Resume.objects.filter(created_by=user).exists():
        user_resume = Resume.objects.filter(created_by=user).first()
        user_resume_skills = user_resume.skills
        vacancies = Vacancies.objects.all()
        recommended_vacancies = []
        for vacancy in vacancies:
            if all(skill in vacancy.description for skill in user_resume_skills):
                recommended_vacancies.append(vacancy)
        serializer = VacanciesDataSerializer(recommended_vacancies, many=True)
        if serializer.data == []:
            serializer = VacanciesDataSerializer(vac, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        serializer = VacanciesDataSerializer(vac, many=True)
        return JsonResponse(serializer.data, safe=False)
