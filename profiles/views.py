from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Applicant, Employer
from .serializers import ApplicantDataSerializer, EmployerDataSerializer, ApplicantDetailSerializer


class ApplicantDataView(APIView):
    def post(self, request):
        applicant = Applicant.objects.create(request.body)
        serializer = ApplicantDataSerializer(applicant)
        return Response(serializer.data)

    def get(self, request):
        applicant = Applicant.objects.all()
        serializer = ApplicantDataSerializer(applicant, many=True)
        return Response(serializer.data)


class ApplicantDetailView(APIView):

    def get(self, request, pk):
        vacancy = Applicant.objects.get(user_id=pk)
        serializer = ApplicantDetailSerializer(vacancy)
        return Response(serializer.data)


class EmployerDataView(APIView):
    def post(self, request):
        employer = Employer.objects.create(request.body)
        serializer = EmployerDataSerializer(employer)
        return Response(serializer.data)

    def get(self, request):
        employer = Employer.objects.all()
        serializer = EmployerDataSerializer(employer, many=True)
        return Response(serializer.data)
