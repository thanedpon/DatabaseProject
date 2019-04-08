from django.shortcuts import render
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
def sign_in(request):
    context = {
        'courses': Course.objects.all(),
        'students': Student.objects.all(),
        'teachers': Teacher.objects.all(),}
    return render(request, 'signin.html', context)
