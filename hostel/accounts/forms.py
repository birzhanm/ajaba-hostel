from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    id_number = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','id_number', 'password1', 'password2',)

class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
