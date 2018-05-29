from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from.models import Profile
from.forms import SecurityQuestionForm

# Create your views here.
def home(request):
    return render(request, 'userprofile/home.html')

def createAccount(request):
    response = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form2 = SecurityQuestionForm
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            q1 = form2.cleaned_data.get('q1')
            user.profile.securityQuestion1 = q1
            #user.profile.securityQuestion2 = form2.cleaned_data.get('q2')
            #user.profile.securityAnswer1 = form2.cleaned_data.get('a1')
            #user.profile.securityAnswer2 = form2.cleaned_data.get('a2')
            user.save()
            login(request, user)
            request.session['name'] = username
            return redirect('/login/')
    else:
        form = UserCreationForm()
        form2 = SecurityQuestionForm()
    return render(request, 'uplift/createAccount.html', {'form': form, 'response': response, 'form2': form2})
