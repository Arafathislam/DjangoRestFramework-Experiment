from django.shortcuts import render
from .models import *
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
def student_detail(request):
    stu=Student.objects.get(id=2)
    seralizer=StudentSerializer(stu)
    json_data= JSONRenderer().render(seralizer.data)

    return HttpResponse(json_data,content_type='application/json')