from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    dob = forms.DateField(help_text="Required format: DD/MM/YYYY")
    class Meta:
        model  = User
        fields =(
            'username',
            'dob',
            'password1',
            'password2', 
            'email',
            # 'image'
        )
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label= 'Display Name'
        # self.fields['email'].label = 'Email Address'

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.name = self.cleaned_data['username']
        user.dob = self.cleaned_data['dob']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model=User
        fields=(
            'first_name',
            'last_name',
            'email',
            # 'image',
        )