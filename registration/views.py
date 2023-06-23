from rest_framework import viewsets
from .serializers import YourModelSerializer
from .models import YourMode


class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
