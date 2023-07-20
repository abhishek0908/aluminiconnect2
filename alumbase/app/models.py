from django.db import models
from django.contrib.auth.models import User

class User_Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    college_reg_no = models.CharField(max_length=20)
    passout_year = models.PositiveIntegerField()
    current_company = models.CharField(max_length=100)
    position_in_company = models.CharField(max_length=100)
    college_branch = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    linkedin = models.URLField(max_length=500)


class JobNews(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company = models.CharField(max_length=70)
    title = models.CharField(max_length=70)
    role = models.TextField(max_length=2000)
    location = models.CharField(max_length=30)
    website_link = models.URLField(max_length=500)
    posted_date = models.DateTimeField(auto_now_add=True)

class InterviewExperience(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     company = models.CharField(max_length=70)
     role = models.CharField(max_length=70)
     experience = models.TextField()
     way_of_preparation = models.TextField()
     Suggestion = models.TextField()
     posted_date = models.DateTimeField(auto_now_add=True)

