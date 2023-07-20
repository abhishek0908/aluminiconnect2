from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Subject,QuestionPaper
from .forms import QuestionPaperForm,CreateSubjectForm
from django.urls import reverse
import os
from django.db.models import Q
def home(request):
    if request.user.is_authenticated:
        fm  =Subject.objects.all()
        return render(request,'prevyear/home.html',{'form':fm})
    else:
        return redirect('/login/')
def view_paper(request, code_no):
  if request.user.is_authenticated:
    question_papers = QuestionPaper.objects.filter(subject_code__code=code_no)
    subject_data = Subject.objects.get(code=code_no)
    return render(request, 'prevyear/allpdf.html', {'information':question_papers,'subject_data':subject_data})
  else:
    return redirect('/login/')


def upload_paper(request, data):
  if request.user.is_authenticated:
    subject_info = get_object_or_404(Subject, code=data)   
    if request.method == 'POST':
        fm = QuestionPaperForm(request.POST, request.FILES)
        if fm.is_valid():      
            year = fm.cleaned_data['year']
            pdf_file = fm.cleaned_data['pdf_file']
            paper_type = fm.cleaned_data['paper_type']
            subject_code = data
            subject_instance = get_object_or_404(Subject, code=subject_code)  # Get the Subject instance
            user = QuestionPaper(paper_type=paper_type, year=year, subject_code=subject_instance, pdf_file=pdf_file)
            user.save()
            return redirect(reverse('prevyear:upload_paper', args=[data]))
            # Redirect to a success page or do any other processing
            # return redirect('success_page')  # Replace 'success_page' with the URL name of your success page
        else:
            # If the form is not valid, print the errors
            print(fm.errors)
    else:
        fm = QuestionPaperForm()
        
    return render(request, 'prevyear/upload_paper.html', {'forms': fm, 'subject_info': subject_info})

  else:
      return request('/login/')
def download_paper(request, paper_id):
  if request.user.is_authenticated:  
    try:
        question_paper = QuestionPaper.objects.get(pk=paper_id)
    except QuestionPaper.DoesNotExist:
        raise Http404

    file_path = question_paper.pdf_file.path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
    else:
        raise Http404
  else:
      return request('/login/')  

def view_pdf(request, paper_id):
  if request.user.is_authenticated:  
    try:
        question_paper = QuestionPaper.objects.get(pk=paper_id)
    except QuestionPaper.DoesNotExist:
        raise Http404

    file_path = question_paper.pdf_file.path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline'  # Display the PDF inline in the browser
            return response
    else:
        raise Http404
  else: 
      return redirect('/login/')  

def delete_pdf(request, paper_id):
  if request.user.is_authenticated:    
    previous_url = request.META.get('HTTP_REFERER')
    request.session['previous_url'] = previous_url
    question_paper = get_object_or_404(QuestionPaper, pk=paper_id)

    # Delete the associated PDF file from storage
    file_path = question_paper.pdf_file.path
    if os.path.exists(file_path):
        os.remove(file_path)

    # Delete the database entry
    question_paper.delete()
    return redirect(previous_url)
  else: 
    return redirect('/login/')    
    

def add_subject(request):
  if request.user.is_authenticated:    
    if request.method=='POST':
        fm = CreateSubjectForm(request.POST)
        if fm.is_valid():
            user = request.user
            code = fm.cleaned_data['code']
            subject_name = fm.cleaned_data['subject_name']
            user  = Subject(user=user,code=code,subject_name=subject_name)
            user.save()
            
            
    else:        
        fm = CreateSubjectForm()
    return render(request,'prevyear/add_subject.html',{'forms':fm})
  else:
     return redirect('/login/')

def search_by_subject(request):
  if request.user.is_authenticated:     
    if request.method=='GET':
        query = request.GET.get('query')
        if query:
            
            fm = Subject.objects.filter(Q(subject_name__icontains=query) | Q(code__icontains=query))
            return render(request,'prevyear/home.html',{'form':fm})
        else:
            return render(request,'prevyear/home.html',{})
  else:
     return redirect('/login/')      