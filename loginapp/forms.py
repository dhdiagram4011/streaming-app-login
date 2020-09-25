from django import forms
from .models import StreamingUser
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

    
class registerForm(forms.ModelForm):
    class Meta:
        model = StreamingUser
        fields = ['username','mails','passwords','phone_numbers']

    username = forms.CharField(label="아이디",widget=forms.TextInput(attrs={'placeholder':'아이디'})) 
    mails = forms.EmailField(label="이메일", widget=forms.TextInput(attrs={'placeholder':'이메일'}))
    passwords = forms.CharField(label="패스워드", widget=forms.PasswordInput(attrs={'placeholder':'패스워드'}))
    phone_numbers = forms.CharField(label="휴대폰번호", widget=forms.TextInput(attrs={'placeholder':'휴대폰번호'}))


class loginForm(forms.ModelForm):
    class Meta:
        model = StreamingUser
        fields = ['email','password']

    mails = forms.EmailField(label="이메일", widget=forms.TextInput(attrs={'placeholder':'이메일'}))
    passwords = forms.CharField(label="패스워드", widget=forms.TextInput(attrs={'placeholder':'패스워드'}))
    

