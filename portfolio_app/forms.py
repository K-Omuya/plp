from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']
        widgets = {
            'title': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the document title',
                'rows': 3,  # You can change this to adjust the height of the text area
                'style': 'resize: none;'  # Optional: Prevent resizing of the textarea
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            }),
        }
