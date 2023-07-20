from django.contrib import admin
from .models import JobNews,InterviewExperience,User_Details
@admin.register(JobNews)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user','company','posted_date']
    
@admin.register(InterviewExperience)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user','company','posted_date']

@admin.register(User_Details)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','user','phone_number','profile_image']