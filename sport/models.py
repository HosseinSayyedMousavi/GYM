from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Action(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(null=True,blank=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class Course(models.Model):
    teacher = models.ForeignKey(User,on_delete=models.CASCADE,related_name='course_teacher')
    student = models.ForeignKey(User,on_delete=models.CASCADE,related_name='course_student')

    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

