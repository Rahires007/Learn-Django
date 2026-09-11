from rest_framework import serializers
from .models import Students

#Students Serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields="__all__"