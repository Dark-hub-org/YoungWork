from .models import Response
from profiles.models import Applicant
from notification.utils import create_notification
from accounts.serializers import UserFromSerializer
from resume.models import Resume
from resume.serializers import ResumeDataSerializer
from .serializers import ResponseDataSerializer
from jobs.models import Vacancies
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from accounts.models import User


@api_view(['POST'])
def response_on_vacancy(request):
    vacancy = request.data.get('vacancy')
    check = Response.objects.filter(created_by=request.user.id, vacancy=vacancy)
    check1 = Vacancies.objects.filter(created_by=request.user.id)
    if (not check) or (not check1):
        serializer = ResponseDataSerializer(data=request.data)
        applicant_get = Applicant.objects.get(user=request.user.id)
        applicant_filter = Applicant.objects.filter(user=request.user.id)
        res = list(applicant_get.response.copy())
        res.append(vacancy)
        applicant_filter.update(response=res)
        if serializer.is_valid():
            serializer.save()
            create_notification(request, 'new_vacancy_response', vacancy_id=vacancy)
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse("Вы не можете откликнуться на вакансию", safe=False)


@api_view(['GET'])
def all_response(request, pk):
    responses = Response.objects.filter(vacancy=pk)

    user_ids = responses.values_list('created_by', flat=True)
    user_data = User.objects.filter(id__in=user_ids)
    resume_data = Resume.objects.filter(created_by__in=user_ids)

    response_serializer = ResponseDataSerializer(responses, many=True)
    user_serializer = UserFromSerializer(user_data, many=True)
    resume_serializer = ResumeDataSerializer(resume_data, many=True)

    data = {
        'response': response_serializer.data,
        'users': user_serializer.data,
        'resumes': resume_serializer.data
    }

    return JsonResponse(data, safe=False)


@api_view(['POST'])
def accepted(request):
    create_notification(request, 'accepted_vacancy_response', vacancyresponse_id=request.data.get('vacancy_response'))
    return JsonResponse({"message": "Accepted"})


@api_view(['POST'])
def view(request):
    create_notification(request, 'view_resume', vacancyresponse_id=request.data.get('vacancy_response'))
    return JsonResponse({"message": "View"})
