from django.db import models

# Create your models here.
class ContLead(models.Model):
    yourname = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at_h = models.DateTimeField(auto_now_add=True)
    
