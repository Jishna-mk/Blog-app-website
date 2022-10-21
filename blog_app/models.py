
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
# class UsersList(models.Model):

    # # Username=models.CharField(max_length=100)
    # email=models.AutoField(primary_key=True)
    # password= models.CharField(max_length = 150)
    # phone_no=models.CharField(max_length=100)
    
class BlogList(models.Model):

    Blog_title=models.CharField(max_length=200)
    Author_name=models.CharField(max_length=200)
    Published_date=models.CharField(max_length=10)
    Blog_detail=models.CharField(max_length=1000)
    Blog_image=models.ImageField(upload_to="blogs")
    Likes=models.IntegerField(default=0)

