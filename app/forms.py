from django import forms
from django.contrib.auth.models import User
from app.models import AtUser

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(
        widget=forms.PasswordInput(), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    userImage = forms.ImageField(help_text="Please enter your real name.",required=False)
    userDept = forms.CharField(help_text="Please enter your Deptment.")
    userJob = forms.CharField(help_text="Please enter your job.")

    class Meta:
        model = AtUser
        fields = ('userImage','userDept','userJob')