from rest_framework import serializers
from .models import NewSms

class SmsSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=20)
    msg = serializers.CharField()

    def create(self, validated_data):
        return NewSms.objects.create(**validated_data)
    
