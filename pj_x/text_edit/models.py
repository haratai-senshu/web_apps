from django.db import models
from django.urls import reverse_lazy
from django.core.validators import FileExtensionValidator
from django.conf import settings
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone

class Post(models.Model):
    file_date_file = models.FileField(upload_to='conversion/', blank=False, null=False, verbose_name='ファイル')
    #python manage.py makemigrations
