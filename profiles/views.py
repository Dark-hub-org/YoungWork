from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Applicant, Employer
from .serializers import ApplicantDataSerializer, EmployerDataSerializer


class ApplicantDataView(APIView):
    def post(self, request):
        applicant = Applicant.objects.create(request.body)
        serializer = ApplicantDataSerializer(applicant)
        return Response(serializer.data)

    def get(self, request):
        applicant = Applicant.objects.create(request.body)
        serializer = ApplicantDataSerializer(applicant)
        return Response(serializer.data)


class EmployerDataView(APIView):
    def post(self, request):
        employer = Employer.objects.create(request.body)
        serializer = EmployerDataSerializer(employer)
        return Response(serializer.data)

    def get(self, request):
        vacancy = Employer.objects.create(request.body)
        serializer = EmployerDataSerializer(vacancy)
        return Response(serializer.data)
