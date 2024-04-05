# Django
from django import forms
from django.contrib.auth.forms import UserCreationForm
# Application
from .models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    email = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)


class SettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('is_subscribed',)
