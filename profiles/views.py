from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Applicant, Employer
from django.shortcuts import render
from .serializers import ApplicantDataSerializer, EmployerDataSerializer, ApplicantDetailSerializer
from rest_framework import status


class ApplicantDataView(APIView):
    def post(self, request, format=None):
        serializer = EmployerDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        applicant = Applicant.objects.all()
        serializer = ApplicantDataSerializer(applicant, many=True)
        return render(request, "index.html", {"summary": serializer})


class ApplicantDetailView(APIView):
    def get(self, request, pk):
        applicant_detail = Applicant.objects.get(pk=pk)
        serializer = ApplicantDetailSerializer(applicant_detail)
        return render(request, "index.html", {"summary": serializer})


class DRFApplicantDetailView(APIView):

    def get(self, request, pk):
        applicant_detail = Applicant.objects.get()
        serializer = ApplicantDetailSerializer(applicant_detail)
        return Response(serializer.data)


class EmployerDataView(APIView):
    def post(self, request, format=None):
        serializer = EmployerDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        employer = Employer.objects.all()
        serializer = EmployerDataSerializer(employer, many=True)
        return render(request, "index.html", {"employer": serializer})


class EmployerDetailView(APIView):

    def get(self, request, pk):
        employer_detail = Employer.objects.get()
        serializer = ApplicantDetailSerializer(employer_detail)
        return render(request, "index.html", {"employer": serializer})


class DRFEmployerDataView(APIView):
    def post(self, request, format=None):
        serializer = EmployerDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        employer = Employer.objects.all()
        serializer = EmployerDataSerializer(employer, many=True)
        return Response(serializer.data)


class DRFEmployerDetailView(APIView):

    def put(self, request, pk, format=None):
        employer = self.get_object(pk)
        serializer = EmployerDataSerializer(employer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        employer_detail = Employer.objects.get()
        serializer = EmployerDataSerializer(employer_detail)
        return Response(serializer.data)
