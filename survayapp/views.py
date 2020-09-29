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

         







