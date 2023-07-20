from django.contrib import admin
from .models import QuestionPaper,Subject

@admin.register(QuestionPaper)
class AdminPdf(admin.ModelAdmin):
    list_display = ['get_subject_code','year','pdf_file']

@admin.register(Subject)
class AdminSubject(admin.ModelAdmin):
    list_display = ['user','code','subject_name']