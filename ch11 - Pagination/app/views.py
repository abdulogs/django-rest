from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.pagination import PageNumberPagination, CursorPagination, LimitOffsetPagination
from rest_framework.response import Response

#  Page = 2
# 6,7,8,9,10 / 100
#  


class pagination(PageNumberPagination):
    page_size = 15
    page_query_param = "page"
    page_size_query_param = "records"
    max_page_size = 1000
    last_page_strings = ('last',)

    def get_paginated_response(self, data):
        return Response({
            "next": self.page.next_page_number() if self.page.has_next() else None,
            "previous": self.page.previous_page_number() if self.page.has_previous() else None,
            "count": self.page.paginator.count,
            "results": data
        })


class paginationlo(LimitOffsetPagination):
    default_offset = 5
    max_limit = 5
    limit_query_param = "page"
    offset_query_param = "records"


class paginationlo(CursorPagination):
    page_size = 5
    ordering = "id"
    cursor_query_param = "page"


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
    pagination_class = pagination
