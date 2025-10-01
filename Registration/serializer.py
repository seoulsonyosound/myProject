from rest_framework import serializers
from .models import userRegistration

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = userRegistration
        fields = '__all__'
        