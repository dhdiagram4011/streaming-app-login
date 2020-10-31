from django.urls import path
from .views import *

app_name = "loginapp"

## localhost:8000/auth/register
## localhost:8000/auth/login

urlpatterns = [
    path('register/', register, name='register'),
    path('login/' , customer_login, name='customer_login'),
    path('registerSuccess/', registerSuccess, name='registerSuccess')
]

