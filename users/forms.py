from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta: #gives a nested namespace for configuration, models affected will be user model
        model = User #interacts with user model, whenever form validates, it is going to create a new User
        fields = ['username', 'email', 'password1', 'password2'] #going to shown in what order in form

#modelform allows us to create form that allows us to work with a database model
#we want a form that updates user model

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
