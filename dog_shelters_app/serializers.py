from rest_framework import serializers
from .models import Dog, Shelter

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'

class ShelterSerializer(serializers.ModelSerializer):
    model = Shelter
    fields = '__all__'