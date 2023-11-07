from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Vacancies, Events
from .serializers import VacanciesDataSerializer, EventsDataSerializer, VacanciesDetailSerializer


class VacanciesDataView(APIView):
    def post(self, request):
        applicant = Vacancies.objects.create(request.body)
        serializer = VacanciesDataSerializer(applicant)
        return Response(serializer.data)

    def get(self, request):
        vacancies = Vacancies.objects.all()
        serializer = VacanciesDataSerializer(vacancies, many=True)
        return Response(serializer.data)


class VacancyDetailView(APIView):

    def get(self, request, pk):
        vacancy = Vacancies.objects.get(user_id=pk)
        serializer = VacanciesDetailSerializer(vacancy)
        return Response(serializer.data)


class EventsDataView(APIView):
    def post(self, request):
        employer = Events.objects.create(request.body)
        serializer = EventsDataSerializer(employer)
        return Response(serializer.data)

    def get(self, request):
        vacancy = Events.objects.create(request.body)
        serializer = EventsDataSerializer(vacancy)
        return Response(serializer.data)
