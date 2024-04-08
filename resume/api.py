from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from accounts.models import User
from .models import Resume
from .serializers import ResumeDataSerializer, ResumeDetailSerializer
from django.shortcuts import render


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def resume_detail_data(request, pk):
    try:
        resume_detail = Resume.objects.get(pk=pk)
    except Resume.DoesNotExist:
        return JsonResponse({'message': 'Resume not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ResumeDetailSerializer(resume_detail)
    return JsonResponse(serializer.data)


@api_view(['GET'])
def resume_of_users(request):
    user = request.user.id
    try:
        resume = Resume.objects.filter(created_by=user).get()
        serializer = ResumeDataSerializer(resume)
        return JsonResponse(serializer.data)
    except Resume.DoesNotExist:
        return JsonResponse({'message': 'Resume not found'}, status=status.HTTP_404_NOT_FOUND)


@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def resume_reg(request):
    serializer = ResumeDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return render(request, "index.html")
    return render(request, "index.html")


@api_view(['GET', 'POST'])
def activate_resume(request):
    if request.method == 'POST':
        Resume.objects.filter(pk=request.data.get('pk')).update(active=True)
    active_resume = Resume.objects.filter(created_by=request.user.id, active=True)
    serializer = ResumeDataSerializer(active_resume, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
def inactivate_resume(request):
    if request.method == 'POST':
        Resume.objects.filter(pk=request.data.get('pk')).update(active=False)
    inactive_resume = Resume.objects.filter(created_by=request.user.id, active=False)
    serializer = ResumeDataSerializer(inactive_resume, many=True)
    return JsonResponse(serializer.data, safe=False)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def ditail_data_of_user(request, pk):
    user = User.objects.get(pk=pk)
    return JsonResponse(data={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'surname': user.surname,
        'region': user.region,
        'citizenship': user.citizenship,
        'phone_number': user.phone_number,
    })


@api_view(['PATCH'])
def edit_resume(request, pk):
    try:
        resume = Resume.objects.get(pk=pk)
    except Resume.DoesNotExist:
        return JsonResponse({'message': 'Resume not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ResumeDataSerializer(instance=resume, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def resume_delete(request, pk):
    resume = Resume.objects.filter(created_by=request.user.id).get(pk=pk)
    resume.delete()
    return JsonResponse({'message': 'resume deleted'})
