from django.db import models
from Photo.models import Photo
# Create your models here.
class CommentModel(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    email = models.EmailField(max_length=200,null=False,blank=False)
    body = models.TextField(max_length=500,null=False,blank=False)
    photo = models.ForeignKey(Photo,on_delete=models.CASCADE,related_name='comment')
    
    def __str__(self):
        return self.name + ' ' + self.body
    