from django.shortcuts import render
from .serializers import NotificationSerializer
from rest_framework import generics, permissions
from .models import Notification

class NotificationsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer
    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        # Mark all notifications as read when they are fetched
        queryset.update(read=True)
        return response.Response(serializer.data)