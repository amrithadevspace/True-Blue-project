from login.models import Login
from rest_framework import serializers


class android_serializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'
