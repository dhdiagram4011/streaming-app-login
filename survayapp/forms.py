from .models import *
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


class nameForm(forms.ModelForm):
    class Meta:
        model = Survay_name
        fields = ['name'] 
        
    name = forms.CharField(max_length=10)


class emailForm(forms.ModelForm):
    class Meta:
        model = Survay_email
        fields = ['email']

    email = forms.EmailField(max_length=100)


class quest01Form(forms.ModelForm):
    class Meta:
        model = Survay_01
        fields = ['question_01']

    question_01 = forms.IntegerField()


class quest02Form(forms.ModelForm):
    class Meta:
        model = Survay_02
        fields = ['question_02']

    question_02 = forms.IntegerField()


class quest03Form(forms.ModelForm):
    class Meta:
        model = Survay_03
        fields = ['question_03']

    question_03 = forms.CharField(max_length=8)


class quest04Form(forms.ModelForm):
    class Meta:
        model = Survay_04
        fields = ['question_04']

    question_04 = forms.IntegerField()


class quest05Form(forms.ModelForm):
    class Meta:
        model = Survay_05
        fields = ['question_05']

    question_05 = forms.IntegerField()


class quest06Form(forms.ModelForm):
    class Meta:
        model = Survay_06
        fields = ['question_06']

    question_06 = forms.IntegerField()


class quest07Form(forms.ModelForm):
    class Meta:
        model = Survay_07
        fields = ['question_07']

    question_07 = forms.CharField(max_length=10)


class quest08Form(forms.ModelForm):
    class Meta:
        model = Survay_08
        fields = ['question_08']

    question_08 = forms.CharField(max_length=10)


class quest09Form(forms.ModelForm):
    class Meta:
        model = Survay_09
        fields = ['question_09']

    question_09 = forms.CharField(max_length=10)

