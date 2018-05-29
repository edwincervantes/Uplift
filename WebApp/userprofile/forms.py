from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SecurityQuestionForm(UserCreationForm):
    ql = forms.CharField(label='Security Question 1', max_length=500)
    a1 = forms.CharField(label='Answer to Question 1', max_length=500)
    q2 = forms.CharField(label='Security Question 2', max_length=500)
    a2 = forms.CharField(label='Answer to Question 2', max_length=500)