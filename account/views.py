from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm,EditProfileForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from . import models

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password= raw_password)
            login(request,user)
            return redirect('account:index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html',{'form':form})

def index(request):
    return render(request, 'account/index.html')

@login_required
def view_profile(request):
    # if pk:
    #     user = User.objects.get(pk=pk)
    # else:
    user = request.user
    args= {'user': user}
    return render(request, 'account/profile.html',args)

@login_required
def edit_profile(request):
    if request.user == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save
            return redirect('account:view_profile')
    else:
        form = EditProfileForm(instance= request.user)
        args = {'form':form}
        return render(request,'account/edit_profile.html',args)

@login_required
def change_password(request):
    if request.user == 'POST':
        form = PasswordChangeForm(request.POST, user=request.user)

        if form.is_valid():
            form.save
            return redirect('account:view_profile')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request,'registration/change_password.html',args)