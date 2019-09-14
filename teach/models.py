from django.db import models

# Create your models here.
class Curriculum(models.Model):
    
    teach_cv = models.FileField(upload_to="cv_teacher/")