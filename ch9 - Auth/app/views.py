from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, BaseAuthentication
from rest_framework.permissions import (IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, DjangoModelPermissions,
DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions, BasePermission)
from rest_framework.decorators import permission_classes, authentication_classes



class myAuthentication(BaseAuthentication):
    def authenticate(self, request):
        return super().authenticate(request)
    
    
    def authenticate_header(self, request):
        return super().authenticate_header(request)


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)
    
    


# For alert popup
@method_decorator(csrf_exempt, name="dispatch")
class StudentBasicApi(viewsets.ModelViewSet):
    # class StudentApi(viewsets.ReadOnlyModelViewSet):
    # For list and retrieve
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]
    permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [AllowAny]


# For drf auth layout
# @method_decorator(csrf_exempt, name="dispatch")
# class StudentBasicApi(viewsets.ModelViewSet):
# # class StudentApi(viewsets.ReadOnlyModelViewSet):
# # For list and retrieve
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]
#     permission_classes = [IsAdminUser]
#     permission_classes = [AllowAny]
#     permission_classes = [IsAuthenticatedOrReadOnly]
