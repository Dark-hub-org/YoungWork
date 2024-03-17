from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from profiles.models import Applicant, Employer
from jobs.models import Vacancies
from resume.models import Resume
from jobs.serializers import VacanciesDataSerializer


@api_view(['GET'])
def me(request):
    try:
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
    except Exception as e:
        return e


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
    User.objects.filter(email=request.data.get('email')).update(avatar=request.data.get('avatar'))
    # user_upload = User.objects.filter(email=request.data.get('email')).values()
    # serializer = AvatarSerializer(data=user_upload)
    # if serializer.is_valid():
    #     serializer.save()
    return JsonResponse({'message': 'success'})


@api_view(['POST'])
def switch_profile(request):
    if request.user.usertype == 'applicant':
        if Employer.objects.filter(user=request.user.id).exists():
            User.objects.filter(id=request.user.id).update(usertype='employer')
            return JsonResponse({'message': 'switch on employer'})
        else:
            Employer.objects.create(user=request.user)
            User.objects.filter(id=request.user.id).update(usertype='employer')
            return JsonResponse({'message': 'switch on employer'})
    else:
        if Applicant.objects.filter(user=request.user.id).exists():
            User.objects.filter(id=request.user.id).update(usertype='applicant')
            return JsonResponse({'message': 'switch on applicant'})
        else:
            Applicant.objects.create(user=request.user)
            User.objects.filter(id=request.user.id).update(usertype='applicant')
            return JsonResponse({'message': 'switch on applicant'})


# TODO: switch fields
@api_view(['GET'])
def recommend(request):
    user = request.user.id
    user_resume = Resume.objects.filter(created_by=user).first()
    if user_resume is None:
        vac = Vacancies.objects.all()
        serializer = VacanciesDataSerializer(vac, many=True)
        return JsonResponse(serializer.data, safe=False)
    user_resume_skills = user_resume.skills
    if Vacancies.objects.filter(description=user_resume_skills).exists():
        vacancies = Vacancies.objects.filter(description=user_resume_skills)
        serializer = VacanciesDataSerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'message': 'No vacancies found for this applicant'})
