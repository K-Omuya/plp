# Generated by Django 5.1.6 on 2025-04-06 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='document',
            new_name='file',
        ),
    ]
