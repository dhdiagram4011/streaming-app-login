from django.db import models
from django.contrib.auth.hashers import make_password, is_password_usable
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



## streaming-service-login model

#회원가입
class StreamingUser(AbstractUser):
    #username = models.CharField(max_length=50)
    mails = models.EmailField(max_length=30)
    passwords = models.CharField(max_length=100)
    phone_numbers = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True, blank=True)


    def publish(self):
        self.published_date = timezone.now()
    
    def __str__(self):
        return self.email



