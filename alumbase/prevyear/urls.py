# pdfapp/urls.py
from django.urls import path
from . import views
app_name = 'prevyear'
urlpatterns = [
    path('',views.home,name='home'),
    path('<slug:code_no>',views.view_paper,name = 'all_papers'),
    path('upload/<slug:data>/',views.upload_paper,name = 'upload_paper'),
    path('download/<int:paper_id>/', views.download_paper, name='download'),
    path('view/<int:paper_id>/', views.view_pdf, name='view'),
    path('delete/<int:paper_id>/', views.delete_pdf, name='delete'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('search_subject/', views.search_by_subject, name='search_subject'),
]
