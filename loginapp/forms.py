from django import forms
from .models import StreamingUser
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

    
class registerForm(forms.ModelForm):
    class Meta:
        model = StreamingUser
        fields = ['email','password','phone_number']

    email = forms.EmailField(label="이메일", widget=forms.TextInput(attrs={'placeholder':'이메일'}))
    password = forms.CharField(label="패스워드", widget=forms.TextInput(attrs={'placeholder':'패스워드'}))
    phone_number = forms.CharField(label="휴대폰번호", widget=forms.TextInput(attrs={'placeholder':'휴대폰번호'}))


class loginForm(forms.ModelForm):
    class Meta:
        model = StreamingUser
        fields = ['email','password']

    email = forms.EmailField(label="이메일", widget=forms.TextInput(attrs={'placeholder':'이메일'}))
    password = forms.CharField(label="패스워드", widget=forms.TextInput(attrs={'placeholder':'패스워드'}))
    

