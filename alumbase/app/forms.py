from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordResetForm,SetPasswordForm
from django import forms
from .models import InterviewExperience,JobNews,User_Details

class PersonRegistration(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Enter Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email']
        labels = {'username':'Enter UserName','first_name':'Enter First Name','last_name':'Enter Last Name','email':'Enter Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),'first_name':forms.TextInput(attrs={'class':'form-control'}),'last_name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'})}
    def __init__(self, *args, **kwargs):
        super(PersonRegistration, self).__init__(*args, **kwargs)
        # Make all fields mandatory
        for field_name in self.fields:
            self.fields[field_name].required = True

class PersonLogin(AuthenticationForm):
   username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
   password = forms.CharField(label='Password', strip = False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User_Details
        fields = ['name', 'phone_number', 'email', 'college_reg_no', 'passout_year','current_company','position_in_company','college_branch','linkedin']
        labels = {
    'name': 'Enter Name',
    'phone_number': 'Enter Mobile Number',
    'email': 'Enter Email',
    'college_reg_no': 'Enter College Registration Number',
    'passout_year': 'Enter Passout Year',
    'current_company': 'Enter Current Company',
    'position_in_company': 'Enter Position in Company',
    'college_branch': 'Enter College Branch',
    'linkedin': 'Enter Your LinkedIn',
    
}
widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'college_reg_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter College Registration Number'}),
            'passout_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Passout Year'}),
            'current_company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Current Company'}),
            'position_in_company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Position in Company'}),
            'college_branch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter College Branch'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
        }

class InterviewExperienceForm(forms.ModelForm):
    class Meta:
        model = InterviewExperience
        fields = ['company', 'role', 'experience', 'way_of_preparation', 'Suggestion']
        labels = {
            'company': 'Company',
            'role': 'Role',
            'experience': 'Experience',
            'way_of_preparation': 'Way of Preparation',
            'Suggestion': 'Suggestion'
        }
        widgets = {
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.Textarea(attrs={'class': 'form-control'}),
            'way_of_preparation': forms.Textarea(attrs={'class': 'form-control'}),
            'Suggestion': forms.Textarea(attrs={'class': 'form-control'}),
        }


class JobFeedForm(forms.ModelForm):
    class Meta:
        model = JobNews
        fields = ['company', 'title', 'role', 'location', 'website_link']

        labels = {
            'company': 'Company Name',
            'title': 'Job Title',
            'role': 'Job Role',
            'location': 'Job Location',
            'website_link': 'Website Link',
        }

        widgets = {
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'website_link': forms.URLInput(attrs={'class': 'form-control'}),
        }

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Enter Registered Email',widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))


class MyPasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}))
    new_password2 = forms.CharField(label='Enter Password Again', widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}))
