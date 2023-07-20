from django.shortcuts import render
from .models import JobNews,InterviewExperience,User_Details
from django.shortcuts import render,HttpResponseRedirect,HttpResponse,redirect
from .forms import PersonRegistration,PersonLogin,UserProfileForm,InterviewExperienceForm,JobFeedForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.db.models import Q
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Error
from allauth.socialaccount.models import SocialApp, SocialToken
from allauth.socialaccount.providers.oauth2.views import OAuth2View
from django.shortcuts import redirect

# /////////////////////////////////////////////////////
# ////////////////////////////////////////////////////



def home(request):
        latest_job = JobNews.objects.order_by('-posted_date')[:3]
        latest_interview = InterviewExperience.objects.order_by('-posted_date')[:3]
        return render(request,'app/home.html',{'jobs':latest_job,'interviews':latest_interview})

# Registration
def registration(request):
     if not request.user.is_authenticated:
        if request.method=='POST':
            fm = PersonRegistration(request.POST)
            if fm.is_valid():
                 email = fm.cleaned_data['email']
                 if User_Details.objects.filter(email=email).exists():
                      messages.error(request,'Email is already registerd')
                 else :
                     user = fm.save()
                     messages.success(request,'You are registerd successfully')
        else :  fm = PersonRegistration()
        return render(request,'app/registration.html',{'forms':fm})
     else:
         return HttpResponseRedirect('/login/')
# ḷogin
def sign_in(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm = PersonLogin(request=request,data= request.POST)
            if fm.is_valid():      
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username,password=password)
                if user is not None:
                    
                    login(request,user)
                    return HttpResponseRedirect('/profile/')
            else : 
                messages.error(request,'Your username or password is wrong')   
        
        else :
            fm = PersonLogin()
        return render(request,'app/login.html',{'forms':fm})
    else :
        return HttpResponseRedirect('/profile/')

# logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def interviewdetails(request,id):
    if request.user.is_authenticated:
        details = InterviewExperience.objects.get(pk=id)
        return render(request,'app/interviewdetails.html',{'info':details})
    else :
        return redirect('/login/')
def all_interview(request):
    if request.user.is_authenticated:
        interview_details= InterviewExperience.objects.all()
    else: 
        return HttpResponseRedirect('/login/')
    return render(request,'app/allinterview.html',{'interview':interview_details})

def alumini_info(request):
   if request.user.is_authenticated: 
    user_info =  User_Details.objects.all().order_by('-passout_year')

    # Set the number of items to display per page
    items_per_page = 3
    paginator = Paginator(user_info, items_per_page)

    page = request.GET.get('page')
    try:
        user_info = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        user_info = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page of results.
        user_info = paginator.page(paginator.num_pages)

    return render(request, 'app/connectpeople.html', {'user_info': user_info})
   else :
       return redirect('/login/')
def job_details(request,id):
    if request.user.is_authenticated:
        job_info = JobNews.objects.get(pk=id)
        return render(request,'app/jobdescription.html',{'info':job_info})
    return redirect('/login/')

def profile(request):
    if request.user.is_authenticated:

      if request.method == 'POST':
        user_info = User_Details.objects.get(user=request.user)
        form = UserProfileForm(request.POST, instance=user_info)
        if form.is_valid():
            form.save()
            user_info.save()
            messages.success(request, 'Profile is updated Successfully') 
        else:
             if 'email' in form.errors.as_data():
                    for error in form.errors.as_data()['email']:
                        if error.code == 'unique':
                            messages.error(request, 'Email is already registered.')
                            
             if 'college_reg_no' in form.errors.as_data():
                    for error in form.errors.as_data()['college_reg_no']:
                        if error.code == 'unique':
                            messages.error(request, 'College Registration Number is already registered.')
        return redirect('profile')    
                
      else : 
            try:
                # Get the User_Details object associated with the logged-in user
                user_info = User_Details.objects.get(user=request.user)
            except User_Details.DoesNotExist:
                # If User_Details does not exist, create a new instance with default values
                user_info = User_Details.objects.create(
                    user=request.user,
                    name=request.user.first_name,
                    phone_number="",
                    email=request.user.email,
                    college_reg_no="",
                    passout_year=0,
                    current_company="",
                    position_in_company="",
                    college_branch="",
                    linkedin="",
                    profile_image=None,
                )   
            # user_info = User_Details.objects.get(user=request.user)          
            fm = UserProfileForm(instance=user_info)
            return render(request, 'app/profile.html', {'form': fm,'user':user_info})
    else :
        return HttpResponseRedirect('/login/')


def add_experience(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = InterviewExperienceForm(request.POST)
            if fm.is_valid():
               experience = fm.save(commit=False)  # Create the object but don't save it yet
               experience.user = request.user  # Associate the logged-in user with the experience
               experience.save()  # Save the object with the associated user
               messages.success(request,'Congartulations! Experience is Published. Click on cancle for go back to home')
        else :  fm = InterviewExperienceForm()
        return render(request,'app/add_experience.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    



def update_experience(request,id):     
      if request.method=='POST':
            pi = InterviewExperience.objects.get(pk=id)
            fm = InterviewExperienceForm(request.POST,instance=pi)
            if fm.is_valid():
                
                fm.save()
                messages.success(request,'Article is Updated Successfully')
                        
      else : 
          pi = InterviewExperience.objects.get(pk=id)
          fm = InterviewExperienceForm(instance=pi)
         
      return render(request,'app/updateexperience.html',{'forms':fm,'id':id})



def all_jobs(request):
 if request.user.is_authenticated:
        jobs= JobNews.objects.all().order_by('-posted_date')
 else: 
    return HttpResponseRedirect('/login/')
 return render(request,'app/all_jobs.html',{'job_details':jobs})



def add_job(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = JobFeedForm(request.POST)
            if fm.is_valid():
                experience = fm.save(commit=False)  # Create the object but don't save it yet
                experience.user = request.user  # Associate the logged-in user with the experience
                experience.save()  # Save the object with the associated user
                job_title = experience.title  # Assuming your model has a 'title' field
                message = f"A new job has been posted: {job_title}. by : {request.user} Check it out!"
                subject = "New Job Posting"

                users_emails = [user.email for user in User_Details.objects.all()]  # Assuming your User model has an 'email' field
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, users_emails, fail_silently=False)
                messages.success(request,'Congartulations! Job is Published. Click on cancle for go back to home')
        else :  fm = JobFeedForm()
        return render(request,'app/add_job.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    

def update_job(request,id):     
      if request.method=='POST':
            pi = JobNews.objects.get(pk=id)
            fm = JobFeedForm(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Job is Updated Successfully')
                        
      else : 
          pi = JobNews.objects.get(pk=id)
          fm = JobFeedForm(instance=pi)
         
      return render(request,'app/update_job.html',{'forms':fm,'id':id})


def search_company(request):
    if request.method=='GET':
        query = request.GET.get('query')
        if query:
            interview_details= InterviewExperience.objects.filter(company__icontains=query)
            return render(request,'app/allinterview.html',{'interview':interview_details})
        else:
            return render(request,'app/allinterview.html',{})
def search_by_people(request):
    if request.method=='GET':
        query = request.GET.get('query')
        if query:
            
            job = User_Details.objects.filter(Q(current_company__icontains=query) | Q(college_branch__icontains=query) | Q(name__icontains=query))
            return render(request,'app/connectpeople.html',{'user_info':job})
        else:
            return render(request,'app/connectpeople.html',{})
        