# forms.py
from django import forms
from .models import QuestionPaper,Subject
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
class QuestionPaperForm(forms.ModelForm):
    class Meta:
        model = QuestionPaper
        fields = ['year', 'paper_type', 'pdf_file']

    # Customizing widgets for each field
    widgets = {
        # 'subject_code': forms.NumberInput(attrs={'class': 'form-control','readonly': True}),
        'year': forms.NumberInput(attrs={'class': 'form-control'}),
        'paper_type': forms.Select(attrs={'class': 'form-control'}),
        'pdf_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }
    current_year = datetime.datetime.now().year 
    year = forms.IntegerField(      
    validators=[
        MinValueValidator(1980, message='Year must be greter than or equal to 1980'),
        MaxValueValidator(current_year, message=f'Year cannot exceed the {current_year}.'),
    ],
    initial=current_year
     # Set the initial value to the current year
)

    # If you want to customize labels for the fields, you can use the labels attribute
    labels = {
        'year': 'Year',
        'paper_type': 'Paper Type',
        'pdf_file': 'PDF File',
    }


class CreateSubjectForm(forms.ModelForm):
      class Meta:
        model = Subject
        fields = ['subject_name', 'code']
        widgets = {
        # 'subject_code': forms.NumberInput(attrs={'class': 'form-control','readonly': True}),
        'code': forms.TextInput(attrs={'class': 'form-control'}),
        'subject_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
        'subject_name': 'Enter Subject Name',
        'code': 'Enter Subject Code',
        }