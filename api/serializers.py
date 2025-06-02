from rest.models import SerializerModel
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SerializerModel
        fields = '__all__'


