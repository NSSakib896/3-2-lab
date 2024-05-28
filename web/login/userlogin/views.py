from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.template import loader

from django.http import HttpResponse

# Create your views here.
# Home page
def index(request):
    return render(request, 'index.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')


def all_user(request):
    text = "Add"
    template = loader.get_template('alluser.html')
    member_list = User.objects.all().values()
    context = {
        'user_list': member_list,
        
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = User.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
    'member': mymember,
    }
    return HttpResponse(template.render(context, request))