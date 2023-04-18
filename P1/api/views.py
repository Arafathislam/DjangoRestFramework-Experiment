from django.shortcuts import render
from .models import *
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.
def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    seralizer=StudentSerializer(stu)
    json_data= JSONRenderer().render(seralizer.data)

    return HttpResponse(json_data,content_type='application/json')


def student_list(request):
    stu=Student.objects.all()
    seralizer=StudentSerializer(stu,many=True)
    # json_data= JSONRenderer().render(seralizer.data)

    # return HttpResponse(json_data,content_type='application/json')

    return JsonResponse(seralizer.data,safe=False)