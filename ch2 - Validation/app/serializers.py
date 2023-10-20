from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    # Validators [1]
    def is_empty(data):
        if data == "":
            raise serializers.ValidationError("Fullname is required")

    id = serializers.IntegerField(read_only=True)
    fullname = serializers.CharField(validators=[is_empty])
    email = serializers.CharField()
    phone = serializers.CharField()


    # Field level validation [2]
    def validate_email(self, value):
        if value == "":
            raise serializers.ValidationError("Email is required")
        return value

    # Object level validation [3]
    def validate(self, data):
        fullname = data.get("fullname")

        if fullname == "":
            raise serializers.ValidationError("Fullname is required")
        return data


    def create(self, validate_date):
        return Student.objects.create(**validate_date)

    def update(self, instance, validate_date):
        instance.fullname = validate_date.get("fullname", instance.fullname)
        instance.email = validate_date.get("email", instance.email)
        instance.phone = validate_date.get("phone", instance.phone)
        instance.save()
        return instance
