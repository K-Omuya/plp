from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('portfolio/', views.portfolio, name='portfolio'),

    path('download/<str:filename>/', views.download_file, name='download_file'),
    path('download/<str:filename>/', views.download_file, name='download_file'),

    path('upload/', views.upload_document, name='upload_document'),
    path('document_list/', views.document_list, name='document_list'),
    path('download/', views.download_page, name='download_page'),
    path('download/<str:filename>/', views.download_file, name='download_file'),
    path('services/', views.services, name='services'),
    path('services/', views.servicess, name='servicess'),
    path('contact/', views.contact, name='contact'),
]
