from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    price = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    davomiyligi = models.IntegerField(default=0)



class Teacher(models.Model):
    full_name = models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=50,null=True,blank=True)
    tajriba = models.IntegerField(default=0)
    subject = models.CharField(max_length=50)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

class Students(models.Model):
    full_name = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=13,null=True,blank=True)
    parents_phone = models.CharField(max_length=30,null=True,blank=True)
    telegram = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)