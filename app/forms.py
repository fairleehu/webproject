# coding=utf-8
from django import forms
from django.contrib.auth.models import User
from app.models import *
from django.contrib.admin import widgets
from django.forms.extras.widgets import SelectDateWidget


class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter your real name!!.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(
        widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    userImage = forms.ImageField(required=False)
    userDept = forms.CharField(help_text="**部")
    userJob = forms.CharField(help_text="员工or管理者")

    class Meta:
        model = AtUser
        fields = ('userImage', 'userDept', 'userJob')


class SendForm(forms.ModelForm):
    sendType = forms.CharField()
    sendText = forms.CharField(widget=forms.Textarea)
    sendTime = forms.DateField()
    sendDept = forms.CharField()

    class Meta:
        model = AtSend
        fields = ('sendType', 'sendText', 'sendTime')

TITLE_CHOICES = (('年假', '年假'),
                 ('事假', '事假'),
                 ('病假', '病假'),)


class LeaveForm(forms.ModelForm):
    leaveName = forms.CharField()
    leaveDept = forms.CharField()
    leaveType = forms.ChoiceField(required=True, choices=TITLE_CHOICES)
    leaveDate = forms.DateTimeField(
        required=True, label='开始时间', widget=forms.extras.widgets.SelectDateWidget)
    leaveFDate = forms.DateTimeField(
        required=True, label='截止时间', widget=forms.extras.widgets.SelectDateWidget)
    leaveText = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = AtLeave
        fields = ('leaveName', 'leaveDept', 'leaveType', 'leaveDate',
                  'leaveFDate', 'leaveText')
