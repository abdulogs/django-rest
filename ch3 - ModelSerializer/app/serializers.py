from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Student
        fields = ["id", "fullname", "email", "phone"]
        # fields = "__all__"
        # exclude = ["id"]
        # read_only_fields = ["fullname"]
        # extra_kwargs = {"fullname": {"read_only": True,"required"= True, validators=[]}}
