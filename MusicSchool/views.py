from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from MusicSchool.models import Student, Teacher, Course, Study, Teach
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

def detail_page_student(request, item_id):
    items = Student.objects.get(id=item_id)
    show_study = Study.objects.all().filter(course_id=item_id)
    return render(request, 'detail.html',{'items':items, 'show_study':show_study})

def detail_page_teacher(request, item_id):
    items = Teacher.objects.get(id=item_id)
    show_teach = Teach.objects.all().filter(course_id=item_id)
    return render(request, 'teacher_detail.html', {'items':items, 'show_teach':show_teach})
