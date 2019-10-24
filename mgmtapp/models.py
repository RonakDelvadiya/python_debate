from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.utils import timezone


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
	
	
class Discussion(models.Model):
    Discussion_Type = (
        ('article','Article'),
        ('question','Question'),
        ('post','Post'),
        ('blog','Blog'),
    )
    title = models.CharField("Title",max_length=100)
    text = models.TextField("Text")
    discussion_type = models.CharField("Type",max_length=10,choices=Discussion_Type)
    added_by = models.ForeignKey(User,default=1)
    is_published = models.BooleanField("Is published",default=True)
    created_date = models.DateTimeField(auto_now_add=True,default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(max_length = 255,upload_to="media/")

    def __str__(self):
	    return self.title


class Comment(models.Model):
    creater = models.ForeignKey(User,related_name='Comm_Creater',default=1)
    discussion = models.ForeignKey(Discussion)
    text = models.TextField("Text",max_length=255)
    added_by = models.ForeignKey(User,blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True,default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
