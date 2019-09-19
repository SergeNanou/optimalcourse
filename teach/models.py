from django.db import models

# Create your models here.
class Curriculum(models.Model):
    
    teach_cv = models.FileField(upload_to="cv_teacher/")

class StudentTest(models.Model):
    level = models.CharField(max_length=30)
    study =  models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)