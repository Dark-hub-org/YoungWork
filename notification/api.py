from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import Notification
from .serializers import NotificationSerializer


@api_view(['POST'])
def read_notification(request, pk):
    notification = Notification.objects.filter(created_for=request.user).get(pk=pk)
    notification.is_read = True
    notification.save()

    return JsonResponse({'message': 'notification read'})


@api_view(['GET'])
def view_notification(request):
    notifications = Notification.objects.filter(created_for=request.user.id)
    serializer = NotificationSerializer(notifications, many=True)
    return JsonResponse(serializer.data, safe=False)
