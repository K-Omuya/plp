from django.shortcuts import render
from django.http import FileResponse, Http404
from django.conf import settings
import os

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def services(request):
    return render(request, 'services.html')

def servicess(request):
    return render(request, 'servicess.html')

def dropdown(request):
    return render(request, 'dropdown.html')

def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render
from .models import Document  # Import your Document model

# views.py
from django.shortcuts import render
from .models import Document  # Assuming Document is the name of your model

def download_page(request):
    documents = Document.objects.all()  # Fetch all documents
    return render(request, 'download_page.html', {'documents': documents})

from django.http import Http404, FileResponse
import os
from django.conf import settings

import os
from django.conf import settings
from django.http import FileResponse, Http404
from .models import Document

def download_file(request, filename):
    # Construct the full file path
    file_path = os.path.join(settings.BASE_DIR, 'myapp', 'static', 'documents', filename)

    # Check if the file exists
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
    else:
        raise Http404("File not found")


from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .forms import DocumentForm

@staff_member_required
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()

    return render(request, 'upload_document.html', {'form': form})


#from django.shortcuts import render
from .models import Document

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'document_list.html', {'documents': documents})



def preview_document(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, 'documents', filename)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    else:
        raise Http404("File not found")


from django import template

register = template.Library()

@register.filter
def split_filename(value):
    """Custom filter to get the filename without the path."""
    return value.split('/')[-1]  # Splitting the path and getting the filename
