from rest_framework.views import APIView
from .models import Applicant, Employer
from django.shortcuts import render
from .serializers import ApplicantDetailSerializer, EmployerDetailSerializer


class ApplicantDetailView(APIView):
    def get(self, request, pk):
        applicant_detail = Applicant.objects.get(pk=pk)
        serializer = ApplicantDetailSerializer(applicant_detail)
        return render(request, "index.html", {"applicant": serializer})


class EmployerDetailView(APIView):

    def get(self, request, pk):
        employer_detail = Employer.objects.get(pk=pk)
        serializer = EmployerDetailSerializer(employer_detail)
        return render(request, "index.html", {"employer": serializer})
