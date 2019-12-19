from django.shortcuts import render
from django.http import HttpResponse
from model_app.models import Students

# Create your views here.
def index(request):
    return HttpResponse("Hey There!")

def home(request):
    return render(request, 'index.html')

def tempTag(request):
    temp = {'temp': 'Template Tag!'}
    return render(request, 'tempTag.html', context= temp)

def student(request):
    student_list = Students.objects.order_by('first_name')
    student_dict = {'students': student_list}
    return render(request, 'student.html', context= student_dict)