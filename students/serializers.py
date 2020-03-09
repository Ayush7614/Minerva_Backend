from rest_framework import serializers

from students.models import Student


class RegisterSerializer(serializers.Serializer):
    class Meta:
        model = Student
        fields = '__all__'