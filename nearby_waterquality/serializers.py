from nearby_waterquality.models import NearbyWaterquality
from rest_framework import serializers


class android_serializer(serializers.ModelSerializer):
    class Meta:
        model = NearbyWaterquality
        fields = '__all__'
