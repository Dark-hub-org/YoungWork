from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Summary
from .serializers import SummaryDataSerializer


class SummaryDataView(APIView):
    def post(self, request):
        applicant = Summary.objects.create(request.body)
        serializer = SummaryDataSerializer(applicant)
        return Response(serializer.data)

    def get(self, request):
        summary = Summary.objects.all()
        serializer = SummaryDataSerializer(summary, many=True)
        return Response(serializer.data)


class SummaryDetailView(APIView):

    def get(self, request, pk):
        summary = Summary.objects.get(user_id=pk)
        serializer = SummaryDataSerializer(summary)
        return Response(serializer.data)
