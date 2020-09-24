form django.urls import path
form .views import *

app_name = "loginapp"

urlpatterns = [
    path('register/', register, name='register'),
    path('login/' , customer_login, name='customer_login'),
]
