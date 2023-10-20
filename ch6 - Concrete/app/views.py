from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# We can make a group of Pk id
class StudentLCApi(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# api/student/ POST 


# api/student/1 PATCH

@method_decorator(csrf_exempt, name="dispatch")
class StudentRUDApi(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
