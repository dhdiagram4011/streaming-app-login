from django.shortcuts import render, redirect
from .models import *
from .forms import *

# class nameForm(forms.ModelForm):
# class emailForm(forms.ModelForm):
# class quest01Form(forms.ModelForm):
# class quest02Form(forms.ModelForm):
# class quest03Form(forms.ModelForm):
# class quest04Form(forms.ModelForm):
# class quest05Form(forms.ModelForm):
# class quest06Form(forms.ModelForm):
# class quest07Form(forms.ModelForm):
# class quest08Form(forms.ModelForm):
# class quest09Form(forms.ModelForm):

    # path('identification/', identification, name='identification'),
    # path('email/', email, name='email'),
    # path('quest01/', quest01, name='quest01'),
    # path('quest02/', quest02, name='quest02'),
    # path('quest03/', quest03, name='quest03'),
    # path('quest04/', quest04, name='quest04'),
    # path('quest05/', quest05, name='quest05'),
    # path('quest06/', quest06, name='quest06'),
    # path('quest07/', quest07, name='quest07'),
    # path('quest08/', quest08, name='quest08'),
    # path('quest09/', quest09, name='quest09'),


def identification(request):
    if request.method == 'GET':
        form = nameForm(request.GET)
        return render(request, 'survayapp/identification.html', {'form':form})
    else:
        form = nameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) 
            name = request.POST['name']
            post.save()
        return redirect('survayapp:email')


def email(request):
    if request.method == 'GET':
        form = emailForm(request.GET)
        return render(request, 'survayapp/email.html', {'form':form})
    else:
        form = emailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            email = request.POST['email']
            post.save()
        return redirect('survayapp:quest01')


def quest01(request):
    if request.method == 'GET':
        form = quest01Form(request.GET)
        return redner(request, 'survayapp/quest01.html', {'form':form})
    else:
        form = quest01Form(request.POST)
        if form.is_valid():
            post = form.save()
            question_01 = request.POST['question_01']
            post.save()
        return redirect('survayapp:quest02')


def quest02(request):
    if request.method == 'GET':
        form = quest02Form(request.GET)
        return render(request, 'survayapp/quest02.html', {'form':form})
    else:
        form = quest02Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            question_02 = request.POST['question_02']
            post.save()
        return redirect('survayapp:quest03')


def quest03(request):
    if request.method == 'GET':
        form = quest03Form(request.GET)
        return render(request, 'survayapp/quest03.html', {'form':form})
    else:
        form = quest03Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            question_03 = request.POST['question_03']
            post.save()
        return redirect('survay:quest04')


def quest04(request):
    if request.method == 'GET':
        form = quest04Form(request.GET)
        return render(request, 'survayapp/quest04.html', {'form':form})
    else:
        form = quest04Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            question_04 = request.POST['question_04']
            post.save()
        return redirect('survayapp:quest05')


def quest05(request):
    if request.method == 'GET':
        form = quest05Form(request.GET)
        return render(request, 'survayapp/quest05.html', {'form':form})
    else:
        form = quest05Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            question_05 = request.POST['question_05']
            post.save()
        return redirect('survayapp:quest06')


def quest06(request):
    if request.method == 'GET':
        form = quest06Form(request.GET)
        return render(request, 'survayapp/quest06.html', {'form':form})
    else:
        form = quest06Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            question_06 = request.POST['question_06']
            post.save()
        return redirect('survayapp:quest07')


def quest07(request):
    if request.method == 'GET':
        form = quest07Form(request.GET)
        return render(request, 'survayapp/quest07.html', {'form':form})
    else:
        form = quest07Form(request.POST)
        post = form.save(commit=False)
        question_07 = request.POST['question_07']
        post.save()
    return redirect('survayapp:quest08')


def quest08(request):
    if request.method == 'GET':
        form = quest08Form(request.GET)
        return render(request, 'survayapp/queest08.html', {'form':form})
    else:
        form = quest08Form(request.POST)
        post = form.save(commit=False)
        question_08 = request.POST['question_08']
        post.save()
    return redirect('survayapp:quest09')


def quest09(request):
    if request.method == 'GET':
        form = quest09Form(request.GET)
        return render(request, 'survayapp/quest09.html', {'form':form})
    else:
        form = quest09Form(request.POST)
        post = form.save(commit=False)
        question_09 = request.POST['question_09']
        post.save()
    return render(request, 'suvrayapp/final.html')














