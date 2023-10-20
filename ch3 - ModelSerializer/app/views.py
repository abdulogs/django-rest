from django.shortcuts import render, HttpResponse
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import io


@method_decorator(csrf_exempt, name="dispatch")
class StudentApi(View):
    def get(self, request, pk=None,  *agrs, **kwargs):
        if pk != None:
            query = Student.objects.get(pk=pk)
            serializer = StudentSerializer(query)
            response = JSONRenderer().render(serializer.data)
        elif pk == None:
            query = Student.objects.all()
            serializer = StudentSerializer(query, many=True)
            response = JSONRenderer().render(serializer.data)

        return HttpResponse(response, content_type="application/json")

    def post(self, request, pk=None, *agrs, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream=stream)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = JSONRenderer().render(serializer.data)
        else:
            response = JSONRenderer().render(serializer.errors)
        return HttpResponse(response, content_type="application/json")

    def put(self, request, pk=None, *agrs, **kwargs):
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream=stream)
        query = Student.objects.get(pk=pk)
        serializer = StudentSerializer(query, data=data)
        if serializer.is_valid():
            serializer.save()
            response = JSONRenderer().render(serializer.data)
        else:
            response = JSONRenderer().render(serializer.errors)
        return HttpResponse(response, content_type="application/json")

    def patch(self, request, pk=None, *agrs, **kwargs):
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream=stream)
        query = Student.objects.get(pk=pk)
        serializer = StudentSerializer(query, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = JSONRenderer().render(serializer.data)
        else:
            response = JSONRenderer().render(serializer.errors)
        return HttpResponse(response, content_type="application/json")

    def delete(self, request, pk=None, *agrs, **kwargs):
        try:
            query = Student.objects.get(pk=pk)
            query.delete()
        except:
            pass
        response = JSONRenderer().render({"message": "Deleted"})
        return HttpResponse(response, content_type="application/json")


# @csrf_exempt
# def studentApi(request, pk=None):
#     if request.method == "GET" and pk != None:
#         query = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(query)
#         response = JSONRenderer().render(serializer.data)
#     elif request.method == "GET" and pk == None:
#         query = Student.objects.all()
#         serializer = StudentSerializer(query, many=True)
#         response = JSONRenderer().render(serializer.data)
#     elif request.method == "POST":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         data = JSONParser().parse(stream=stream)
#         serializer = StudentSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response = JSONRenderer().render(serializer.data)
#         else:
#             response = JSONRenderer().render(serializer.errors)
#     elif request.method == "PATCH":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         data = JSONParser().parse(stream=stream)
#         query = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(query, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             response = JSONRenderer().render(serializer.data)
#         else:
#             response = JSONRenderer().render(serializer.errors)
#     elif request.method == "PUT":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         data = JSONParser().parse(stream=stream)
#         query = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(query, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response = JSONRenderer().render(serializer.data)
#         else:
#             response = JSONRenderer().render(serializer.errors)
#     elif request.method == "DELETE":
    #     try:
    #         query = Student.objects.get(pk=pk)
    #         query.delete()
    #     except:
    #         pass
    #     response = JSONRenderer().render({"message": "Deleted"})
    # return HttpResponse(response, content_type="application/json")
