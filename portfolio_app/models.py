# models.py
from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')

    @property
    def file_type(self):
        return self.file.name.split('.')[-1].upper()  # Get the file extension

    def __str__(self):
        return self.title
