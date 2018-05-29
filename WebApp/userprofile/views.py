from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .forms import SecurityQuestionForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'userprofile/home.html')

def createAccount(request):
    response = ''
    if request.method == 'POST':
        form2 = SecurityQuestionForm(request.POST)
        if form2.is_valid():
            form2.save()
            username = form2.cleaned_data.get('username')
            raw_password = form2.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            request.session['name'] = username
            user = User.objects.get(username=username)
            user.profile.securityQuestion1 = "Why aren't you working?"
            user.profile.securityAnswer1 = form2.cleaned_data.get('a1')
            user.profile.securityQuestion2 = form2.cleaned_data.get('q2')
            user.profile.securityAnswer2 = form2.cleaned_data.get('a2')
            user.save()
            return redirect('/uplift/')
    else:
        form2 = SecurityQuestionForm()
    return render(request, 'userprofile/createAccount.html', {'response': response, 'form2': form2})
