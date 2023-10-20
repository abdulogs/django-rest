from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView, api_view
from rest_framework import status


@method_decorator(csrf_exempt, name="dispatch")
class StudentApi(APIView):
    def get(self, request, pk=None,  *agrs, **kwargs):
        if pk != None:
            query = Student.objects.get(pk=pk)
            serializer = StudentSerializer(query)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif pk == None:
            query = Student.objects.all()
            serializer = StudentSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk=None, *agrs, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, *agrs, **kwargs):
        query = Student.objects.get(pk=pk)
        serializer = StudentSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def patch(self, request, pk=None, *agrs, **kwargs):
        query = Student.objects.get(pk=pk)
        serializer = StudentSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk=None, *agrs, **kwargs):
        try:
            query = Student.objects.get(pk=pk)
            query.delete()
        except:
            pass
        return Response({"message": "Deleted"})


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
@csrf_exempt
def studentApi(request, pk=None):
    if request.method == "GET" and pk != None:
        query = Student.objects.get(pk=pk)
        serializer = StudentSerializer(query)
        return Response(serializer.data)
    elif request.method == "GET" and pk == None:
        query = Student.objects.all()
        serializer = StudentSerializer(query, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == "PATCH":
        query = Student.objects.get(pk=pk)
        serializer = StudentSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == "PUT":
        query = Student.objects.get(pk=pk)
        serializer = StudentSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == "DELETE":
        try:
            query = Student.objects.get(pk=pk)
            query.delete()
        except:
            pass
        return Response({"message": "Deleted"})
