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

class Diet(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class Plan(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    action = models.ForeignKey(Action,on_delete=models.CASCADE)
    set_number = models.PositiveIntegerField()
    number_per_set = models.PositiveIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    day_of_week = models.CharField(max_length=10 , choices=(('saturday','saturday'),
                                                                                                                ('sunday','sunday'),
                                                                                                                ('monday','monday'),
                                                                                                                ('tuesday','tuesday'),
                                                                                                                ('wednesday','wednesday'),
                                                                                                                ('thursday','thursday'),
                                                                                                                ('friday','friday')))

    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)