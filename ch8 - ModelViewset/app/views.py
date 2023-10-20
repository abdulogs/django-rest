from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name="dispatch")
class StudentApi(viewsets.ModelViewSet):
# class StudentApi(viewsets.ReadOnlyModelViewSet):
# For list and retrieve
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

