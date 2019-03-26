from django.db import models
from datetime import datetime
# Create your models here.
class Teacher(models.Model):
    Tname = models.CharField(max_length=255)
    Tnname = models.CharField(max_length=255)
    Tsex = models.CharField(max_length=255)
    def __str__(self):
        return self.Tname

class Student(models.Model):
    Sname = models.CharField(max_length=255)
    Snname = models.CharField(max_length=255)
    Age = models.IntegerField(default=0)
    Ssex = models.CharField(max_length=255)
    Pnum = models.IntegerField(default=0)
    def __str__(self):
        return self.Sname

class Course(models.Model):
    Cname = models.CharField(max_length=255)
    Hours = models.IntegerField(default=0)
    def __str__(self):
        return self.Cname

class Study(models.Model):
    Startd = models.DateTimeField(default=datetime.now, blank=True)
    Stopd = models.DateTimeField(default=datetime.now, blank=True)
    Learnday = models.CharField(max_length=255)
    Learnhour = models.CharField(max_length=255)
    Level = models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Teach(models.Model):
    Teachday = models.CharField(max_length=255)
    Teachhour = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

