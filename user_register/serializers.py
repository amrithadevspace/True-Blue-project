from user_register.models import User
from rest_framework import serializers

class android_serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
