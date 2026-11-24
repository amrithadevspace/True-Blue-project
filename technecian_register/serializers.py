from technecian_register.models import Technecian
from rest_framework import serializers


class android_serializer(serializers.ModelSerializer):
    class Meta:
        model = Technecian
        fields = '__all__'
