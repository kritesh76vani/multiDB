from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from CustomUsers.models import CustomUser


DB_CHOICES = (('database1', 'DATABASE 1'),
              ('database2', 'DATABASE 2'),
              ('database3', 'DATABASE 3'),
              ('database4', 'DATABASE 4'),
              ('database5', 'DATABASE 5'))


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','databases' )