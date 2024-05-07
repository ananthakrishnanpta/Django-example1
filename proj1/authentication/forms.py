from django import forms
from django.contrib.auth.models import User 


class RegisterationForm(forms.ModelForm):

    password_ = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','password','password_', 'email']
        
        