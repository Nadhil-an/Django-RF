from rest.models import SerializerModel
from employees.models import employee
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SerializerModel
        fields = '__all__'

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'


