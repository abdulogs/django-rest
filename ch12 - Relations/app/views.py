from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny



@method_decorator(csrf_exempt, name="dispatch")
class StudentBasicApi(viewsets.ModelViewSet):
# class StudentApi(viewsets.ReadOnlyModelViewSet):
# For list and retrieve
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]
    permission_classes = [IsAuthenticatedOrReadOnly]

