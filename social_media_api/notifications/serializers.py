from rest_framework import serializers
from .models import Notification
from accounts.serializers import UserSerializer


class NotificationSerializer(serializers.ModelSerializer):   
    recipient = UserSerializer(read_only=True)
    author = UserSerializer(read_only=True)
    target = serializers.SerializerMethodField()


    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'author', 'verb', 'target', 'timestamp', 'read']
        read_only_fields = ['id', 'recipient', 'author', 'verb', 'target', 'timestamp', 'read']