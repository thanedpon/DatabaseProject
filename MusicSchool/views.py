from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from MusicSchool.models import Student, Teacher
# Create your views here.
def index(request):
    header_str ='Hello,Welcome to Music School'
    context = {
        'var1': header_str
    }
    return render(request, 'index.html', context)
def student_page(request):
    student_item = Student.objects.all()
    return render(request,'student.html', {'student_item':student_item})

def teacher_page(request):
    teacher_item = Teacher.objects.all()
    return render(request,'teacher.html', {'teacher_item':teacher_item})

