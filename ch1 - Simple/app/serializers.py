from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname = serializers.CharField()
    email = serializers.CharField()
    phone = serializers.CharField()

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.fullname = validate_data.get("fullname", instance.fullname)
        instance.email = validate_data.get("email", instance.email)
        instance.phone = validate_data.get("phone", instance.phone)
        instance.save()
        return instance
