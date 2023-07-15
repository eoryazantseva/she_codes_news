# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # changes, that we are going to make to the userform
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
        
class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

# every time we update a model, we need to make migrations so that the changes are applied to the db