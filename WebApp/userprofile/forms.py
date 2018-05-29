from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SecurityQuestionForm(UserCreationForm):
    ql = forms.CharField(max_length=500, label='Security Question 1')
    q2 = forms.CharField(max_length=500, label='Security Question 2')
    a1 = forms.CharField(max_length=500, label='Answer to Question 1')
    a2 = forms.CharField(max_length=500, label='Answer to Question 2')
