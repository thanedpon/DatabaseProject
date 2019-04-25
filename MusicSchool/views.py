from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from MusicSchool.models import Student, Teacher, Course, Study, Teach
from django.shortcuts import render_to_response

def index(request):
    context = {
        'courses': Course.objects.all(),
        'students': Student.objects.all(),
        'teachers': Teacher.objects.all(),}
#        'teaches' : Teach.objects.all().filter(),
#        'items': Teacher.objects.get(id=item_id),
#        'show_teach': Teach.objects.all().filter(id=item_id)
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

def addStudent(request):
        if request.method == 'POST':
                add_student = Student(Sname=request.POST.get('s_name',''),
                Ssurname = request.POST.get('s_surname',''),
                Snickname=request.POST.get('s_nickname',''),
                Age=request.POST.get('s_age',''),
                Pnum=request.POST.get('s_pnum',''),
                Ssex=request.POST.get('s_sex',''))
                add_student.save()
                return redirect('http://localhost:8000/')
        return render(request, 'addStudent.html')

def addTeacher(request):
        if request.method == 'POST':
                add_teacher = Teacher(Tname=request.POST.get('t_name',''),
                Tsurname = request.POST.get('t_surname',''),
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

def addTeach(request):
        context = {
             'course': Course.objects.all(),
             'teacher': Teacher.objects.all(),
         }
        #check = Teacher.objects.only('id').get(id=teacher_get_id)
        #print ('check:', check)
        if request.method == 'POST':
            teacher_get_id = request.POST.get('t2','')
            x = Teacher.objects.filter(Tname=teacher_get_id)[0]
            course_get_id = request.POST.get('course','')
            y = Course.objects.filter(Cname=course_get_id)[0]
            add_teach = Teach(course=y,
            teacher = x,
            Teach_day = request.POST.get('day',''),
            Teach_hour= request.POST.get('hour',''))
            add_teach.save()
            return redirect('http://localhost:8000/')
        return render(request, 'addTeach.html',context)

def addStudy(request):
        context = {
            'course': Course.objects.all(),
            'student': Student.objects.all(),
        }
        if request.method == 'POST':
            study_get_id = request.POST.get('student','')
            Studyid = Student.objects.filter(Sname=study_get_id)[0]
            course_get_id = request.POST.get('course','')
            Courseid = Course.objects.filter(Cname=course_get_id)[0]
            add_study = Study(student=Studyid,
            course = Courseid,
            Startd = request.POST.get('startday',''),
            Stopd = request.POST.get('stopday',''),
            Learn_day = request.POST.get('Learnday', ''),
            Learn_hour = request.POST.get('Learnhour', ''),
            Level = request.POST.get('level', ''),
            period = request.POST.get('period',''))
            add_study.save()
            return redirect('http://localhost:8000/')
        return render(request, 'addStudy.html', context)
