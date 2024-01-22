from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MyUser
from .serializers import MyUserDataSerializer


class MyUserDataView(APIView):
    def get(self, request):
        User = MyUser.objects.all()
        serializer = MyUserDataSerializer(User, many=True)
        return Response(serializer.data)
