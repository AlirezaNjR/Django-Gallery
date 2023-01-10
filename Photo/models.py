from django.db import models
from django.urls import reverse
from Accounts.models import CustomUser
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model

class Photo(models.Model):
    title = models.CharField(max_length=250,blank=False,null=False,default='')
    body = models.TextField(max_length=900,blank=False,null=False,default='')
    # slug = models.SlugField(max_length=250,unique_for_date='date')
    image = models.ImageField(upload_to = 'Photos/%y,%m,%d',blank=False,null=False)
    photo_grapher = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=False,blank=False)
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=50,choices=CustomUser.LOCATIONS,blank=True,null=True)
    tags = TaggableManager(related_name='Tags')

    def get_absolute_url(self):
        return reverse("Gallery:Detail", kwargs={"pk": self.id})
    
    def __str__(self):
        return self.title

