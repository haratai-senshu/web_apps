from .models import Post
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.conf import settings


class UploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('file_date_file',)
