from django.db import models

# Create your models here.
class Message(models.Model):
    user = models.CharField(max_length=30)
    sujet = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    email = models.CharField(max_length=30)
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Message"

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.user,
                                          self.sujet,
                                          self.message,
                                          self.email,
                                          self.created_at,
                                          self.phone)