from django.shortcuts import render
from .models import StreamingUser
from django.template.loader import redner_to_string
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
            email = request.POST["email"]
            password = request.POST["password"]
            phone_number = request.POST["phone_number"]
            post.set_password(password)
            post.save()
        return redirect('loginapp:registerSuccess')


def registerSuccess(request):
    customer_lists = StreamingUser.objects.filter(created_date__lte=timezone.now().order_by('-created_date')[:1]
    return render(request, 'loginapp/register_success.html', {'customer_lists':customer_lists})



## 로그인
def customer_login(request):
    if request.method == 'GET':
        form = loginForm()
        return render(request, 'loginapp/login.html', {'form':form})
    elif request.method == 'POST':
        email = request.POST.get('email','')
        password = request.POST.get('password','')

        user = authenticate(email=email, password=password)

        if email is not None:
            login(request, user)
            return redirect('')
        else:
            return render(request, '')


