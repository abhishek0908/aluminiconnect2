from django.urls import path
from . import views
from. import allauth
from .forms import MyPasswordResetForm,MyPasswordResetConfirmForm
from django.contrib.auth.views import PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView,PasswordResetView
urlpatterns = [
path('',views.home,name='home'),
path('interviewdetails/<int:id>/',views.interviewdetails,name='interviewdetail'),
path('allinterview/',views.all_interview,name='allinterview'),
path('aluminiinfo/',views.alumini_info,name='aluminiinfo'),
path('description/<int:id>/',views.job_details,name='jobdescription'),
path('alljobs/',views.all_jobs,name='all_jobs'),
path('login/',views.sign_in,name='login'),
path('logout/',views.user_logout,name='logout'),
path('registration/',views.registration,name='registration'),
path('profile/',views.profile,name='profile'),
path('addexperince/',views.add_experience,name='add_experience'),
path('addjob/',views.add_job,name='add_job'),
path('update_experience/<int:id>',views.update_experience,name='update_experience'),
path('update_job/<int:id>',views.update_job,name='update_job'),
path('search/',views.search_company,name='search_company'),
path('searchpeople/',views.search_by_people,name='search_people'),
path('password-reset/',PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
path('password-reset/done/',PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
path('password-reset-confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MyPasswordResetConfirmForm), name='password_reset_confirm'),
path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
path('social-login/', allauth.social_login, name='social_login'),]

