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
    
    class Meta:
        verbose_name = "Message"

    def __str__(self):
        return '{} {} {} {} {}'.format(self.sujet_h,
                                       self.message_h,
                                       self.email_h,
                                       self.created_at_h,
                                       self.phone_h)
class Comment(models.Model):
    user = models.CharField(max_length=30)
    forum = models.ForeignKey(Quest_ans, on_delete=models.CASCADE)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)