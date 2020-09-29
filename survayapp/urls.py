from django.urls import path
from .views import *

app_name = "survayapp"

urlpatterns = [
    path('identification/', identification, name='identification'),
    path('email/', email, name='email'),
    path('quest01/', quest01, name='quest01'),
    path('quest02/', quest02, name='quest02'),
    path('quest03/', quest03, name='quest03'),
    path('quest04/', quest04, name='quest04'),
    path('quest05/', quest05, name='quest05'),
    path('quest06/', quest06, name='quest06'),
    path('quest07/', quest07, name='quest07'),
    path('quest08/', quest08, name='quest08'),
    path('quest09/', quest09, name='quest09'),
]



