from django.shortcuts import render
from myapi.models import Student
from myapi.serializer import StudentSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer

# Create your views here.

def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    return JsonResponse(serializer.data)