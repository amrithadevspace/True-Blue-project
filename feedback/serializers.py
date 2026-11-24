from feedback.models import Feedback
from rest_framework import serializers


class android_serializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
