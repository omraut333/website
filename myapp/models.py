from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    mobile = models.CharField(max_length=12)
    msg = models.TextField()

class blog(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    user_name = models.ForeignKey(User, on_delete= models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    blog_name = models.ForeignKey(blog, on_delete= models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)


class projects_data(models.Model):
    pic = models.ImageField(upload_to='images/')
    pro_name = models.CharField(max_length=150)
    start_date = models.DateTimeField(auto_now= False)
    end_date = models.DateTimeField(auto_now=False)
    desc = models.TextField()

class experience_data(models.Model):
    name = models.CharField(max_length=120)
    organisation = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    desc = models.TextField()

class education_data(models.Model):
    edu_name = models.CharField(max_length=120)
    clg_name = models.CharField(max_length=120)
    uni_name = models.CharField(max_length=120)
    passing = models.DateField(auto_now=False)
    marks = models.CharField(max_length=10)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/')

class home_data(models.Model):
    image = models.ImageField(upload_to='images/')
    tag = models.CharField(max_length=120)
    desc = models.TextField()

class about_me_data(models.Model):
    desc = models.TextField()
    image = models.ImageField(upload_to='images/')

class extra_data(models.Model):
    list = models.TextField()