from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


@method_decorator(csrf_exempt, name="dispatch")
class StudentBasicApi(viewsets.ModelViewSet):
    # class StudentApi(viewsets.ReadOnlyModelViewSet):
    # For list and retrieve
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["id", "fullname", "email", "phone"] 
    # ?fullname=abc&email=abc@gmail.com
    search_fields = ["fullname", "email", "phone"]
    # ?search=abc&search=abc@gmail.com
    ordering_fields = ["id"]
    # ? -id


# fetch("url", {
# method: "GET",
# data: {
# email: "john",
# fullname: ""
# }
# })

    def get_queryset(self):
        return super().get_queryset()


"""
"^" starts with
"=" Exact
"@" full text in postgresql
"$" regex

"""
