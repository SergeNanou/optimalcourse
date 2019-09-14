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
# Create your models here.
class Quest_ans(models.Model):
    user_h = models.CharField(max_length=30)
    sujet_h = models.CharField(max_length=100)
    message_h = models.TextField(max_length=500)
    email_h = models.CharField(max_length=30)
    phone_h = models.IntegerField()
    created_at_h = models.DateTimeField(auto_now_add=True)
    answer_h_0 = models.TextField(max_length=500, blank=True)
    answer_h_1 = models.TextField(max_length=500, blank=True)
    answer_h_2 = models.TextField(max_length=500, blank=True)
    answer_h_3 = models.TextField(max_length=500, blank=True)
    
    class Meta:
        verbose_name = "Message"

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.user,
                                          self.sujet,
                                          self.message,
                                          self.email,
                                          self.created_at,
                                          self.phone)