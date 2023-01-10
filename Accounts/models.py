from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class CustomUser(AbstractUser):
    GENDER = (
        ('مرد','مرد'),
        ('زن','زن'),
        ('دیگر','دیگر'),
    )

    LOCATIONS = (
        ('ایران','ایران'),
        ('آمریکا','آمریکا'),
        ('ترکیه','ترکیه'),
        ('روسیه','روسیه'),
        ('کره','کره'),
    )
    
    gender = models.CharField(max_length=10,choices=GENDER,blank=True,null=True,default='دیگر')
    avatar = models.ImageField(upload_to='UsersAvatar/%y,%m,%d',blank=True,null=True)
    location = models.CharField(max_length=50,choices=LOCATIONS,blank=True,null=True)
    age = models.CharField(max_length=3)

    def get_absolute_url(self):
        return reverse("Accounts:Profile", kwargs={"pk": self.id})

