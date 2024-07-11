from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=52, verbose_name='Name')
    #video = models.FileField(upload_to='video', verbose_name='Upload video')
    created_by = models.ForeignKey(User, verbose_name='Created by', 
                       related_name="create_%(class)s", on_delete=models.SET_NULL,null=True,blank=True)
    user_likes = models.ManyToManyField(User, null=True, 
                  blank=True, help_text='User can like once', 
                         verbose_name='Like by')