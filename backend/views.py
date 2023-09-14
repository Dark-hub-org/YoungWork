from rest_framework.views import APIView
from django.shortcuts import render


class Site(APIView):
    def index(request):
        return render(request, "index.html")
