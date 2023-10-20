from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



# We can make a group of Pk id

class StudentListApi(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StudentSingleApi(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


@method_decorator(csrf_exempt, name="dispatch")
class StudentCreateApi(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@method_decorator(csrf_exempt, name="dispatch")
class StudentUpdateApi(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


@method_decorator(csrf_exempt, name="dispatch")
class StudentDeleteApi(GenericAPIView,  DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
