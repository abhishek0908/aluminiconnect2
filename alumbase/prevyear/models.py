from django.db import models
from django.contrib.auth.models import User
Exam_type = (
        ('Mid', 'Mid Semester'),
        ('End', 'End Semester'),
        ('Quiz1', 'First Quiz'),
        ('Quiz2', 'Second Quiz'),
    )
class Subject(models.Model):
    user  = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    code = models.CharField(primary_key=True, max_length=20)
    subject_name = models.CharField(max_length=100)

class QuestionPaper(models.Model):
    subject_code = models.ForeignKey(Subject, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    paper_type = models.CharField(max_length=5, choices=Exam_type,default='mid')
    pdf_file = models.FileField(upload_to='question_papers/')
    def get_subject_code(self):
        return self.subject_code.code