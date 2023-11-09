from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Summary
from .serializers import SummaryDataSerializer
from rest_framework import status


class SummaryDataView(APIView):
    def post(self, request, format=None):
        serializer = SummaryDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        summary = Summary.objects.all()
        serializer = SummaryDataSerializer(summary, many=True)
        return render(request, "index.html", {"summary": serializer})


class DRFSummaryDataView(APIView):
    def post(self, request, format=None):
        serializer = SummaryDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        summary = Summary.objects.all()
        serializer = SummaryDataSerializer(summary, many=True)
        return Response(serializer.data)


class SummaryDetailView(APIView):

    def get(self, request, pk):
        summary_detail = Summary.objects.get(user_id=pk)
        serializer = SummaryDataSerializer(summary_detail)
        return render(request, "index.html", {"summary_detail": serializer})


class DRFSummaryDetailView(APIView):

    def get(self, request, pk):
        summary_detail = Summary.objects.get(user_id=pk)
        serializer = SummaryDataSerializer(summary_detail)
        return Response(serializer.data)
