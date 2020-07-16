from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

from .forms import SignUpForm,EditProfileForm
from account.models import Profile,Friend
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

# def index(request):
#     return render(request, 'account/index.html')
class IndexView(TemplateView):
    @method_decorator(login_required)

    def get(self,request):
        users = User.objects.exclude(id=request.user.id)
        # friend = get_object_or_404(Friend,current_user=request.user)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
        args = {'users':users, 'friends':friends}
        return render(request, 'account/index.html',args)

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


def add_friend(request,operation,pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user,friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user,friend)
    return redirect('account:index')