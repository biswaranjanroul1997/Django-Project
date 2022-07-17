from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DeleteView
from django.http import HttpResponse
from django.views.generic import TemplateView
# from django.contrib.auth import User,auth
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Registration sucessfull.")
            return redirect("login")
        messages.error(request,"Unsucessful registration. Invalid Information.")
    form = NewUserForm()
    return render(request, template_name = 'register.html', context ={'register_form':form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                # messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    form = AuthenticationForm()
    return render(request, template_name ='login.html' ,context ={"login_form" : form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have Sucessfully logged out.")
    return redirect("login")
