from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from MusicSchool.models import Student, Teacher, Course, Study, Teach
from django.shortcuts import render_to_response
#from django.contrib import user
# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all(),
        'students': Student.objects.all(),
        'teachers': Teacher.objects.all(),
#        'teaches' : Teach.objects.all().filter(),
#        'items': Teacher.objects.get(id=item_id),
#        'show_teach': Teach.objects.all().filter(id=item_id)
 }
#    print (context[teaches])
    return render(request, 'index.html', context)

def detail_page_student(request, item_id):
    context = {
        'courses': Course.objects.all(),
        'students': Student.objects.all(),
        'teachers': Teacher.objects.all(),
        'items' : Student.objects.get(id=item_id),
        'show_study' : Study.objects.all().filter(student_id=item_id)}
    return render(request, 'detail.html',context)

def detail_page_teacher(request, item_id):
    context = {
        'courses': Course.objects.all(),
        'students': Student.objects.all(),
        'teachers': Teacher.objects.all(),
        'items' : Teacher.objects.get(id=item_id),
        'show_teach' : Teach.objects.all().filter(teacher_id=item_id)}
#    return render(request, 'teacher_detail.html', {'items':items, 'show_teach':show_teach})
    return render(request, 'teacher_detail.html', context)

#def course(request, item_id):
#    context = {
#        'courses': Course.objects.all(),
#        'students': Student.objects.all(),
#        'teachers': Teacher.objects.all(),
#    }
#    return render_to_response('course.html',context)

def addData(request):
        return render(request, 'addData.html')
def addStudent(request):
        if request.method == 'POST':
                add_student = Student(Sname=request.POST.get('s_name',''),
                Snickname=request.POST.get('s_nickname',''),
                Age=request.POST.get('s_age',''),
                Pnum=request.POST.get('s_pnum',''),
                Ssex=request.POST.get('s_sex',''))
                add_student.save()
                return redirect('http://localhost:8000/')
        return render(request, 'addStudent.html')

def addTeacher(request):
        if request.method == 'POST':
                add_teacher = Teacher(Tname=request.POST.get('s_name',''),
                Tnickname=request.POST.get('t_nickname',''),
                Temail=request.POST.get('t_email',''),
                Ttel=request.POST.get('t_pnum',''),
                Tsex=request.POST.get('t_sex',''))
                add_teacher.save()
                return redirect('http://localhost:8000/')
        return render(request, 'addTeacher.html')

def addCourse(request):
        if request.method == 'POST':
                add_course = Course(Cname=request.POST.get('c_name',''),
                Hours=request.POST.get('h',''),
                Price=request.POST.get('p',''))
                add_course.save()
                return redirect('http://localhost:8000/')
        return render(request, 'addCourse.html')



        
