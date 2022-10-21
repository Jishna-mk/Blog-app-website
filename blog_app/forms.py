
from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import BlogList

class UserAddForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class BlogListForm(ModelForm):
    class Meta:
        model=BlogList
        fields="__all__"