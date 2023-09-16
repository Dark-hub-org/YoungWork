from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Applicant
from .serializer import ApplicantDataSerializer


class ApplicantDataView(APIView):

    def post(self, request):
        vacancy = Applicant.objects.create(request.body)
        serializer = ApplicantDataSerializer(vacancy)
        return Response(serializer.data)

    def get(self, request):
        vacancy = Applicant.objects.all()
        serializer = ApplicantDataSerializer(vacancy, many=True)
        return Response(serializer.data)
