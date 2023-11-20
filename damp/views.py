from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from .models import DampUser
from rest_framework import status
from .serializers import *


class DRFDampUserDataView(APIView):
    def post(self, request, format=None):
        serializer = DampUserDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        applicant = DampUser.objects.all()
        serializer = DampUserDataSerializer(applicant, many=True)
        return Response(serializer.data)


class DRFDampUserDetailView(APIView):

    def get(self, request, pk):
        applicant_detail = DampUser.objects.get(user_id=pk)
        serializer = DampUserDetailSerializer(applicant_detail)
        return Response(serializer.data)
