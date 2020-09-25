from django.shortcuts import render, redirect
from .models import StreamingUser
from django.template.loader import render_to_string
from django.contrib.auth.hashers import make_password
from .forms import registerForm, loginForm 
from django.contrib.auth import login, authenticate


#registerForm , loginForm

#회원가입
def register(request):
    if request.method == 'GET':
        form = registerForm(request.GET)
        return render(request, 'loginapp/register.html', {'form':form})
    elif request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            username = request.POST["username"]
            mails = request.POST["mails"]
            passwords = request.POST["passwords"]
            phone_numbers = request.POST["phone_numbers"]
            post.set_password(passwords)
            post.save()
        #return redirect('loginapp:registerSuccess')
        return render(request, 'loginapp/register_success.html')

def registerSuccess(request):
    customer_lists = StreamingUser.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:1]
    #return render(request, 'loginapp/register_success.html', {'customer_lists':customer_lists})
    return render(request, 'loginapp/register_success.html')


## 로그인
def customer_login(request):
    if request.method == 'GET':
        form = loginForm()
        return render(request, 'loginapp/login.html', {'form':form})
    elif request.method == 'POST':
        mails = request.POST.get('mails','')
        passwords = request.POST.get('passwords','')

        user = authenticate(mails=mails, passwords=passwords)

        if mails is not None:
            login(request, user)
            return redirect('')
        else:
            return render(request, '')

