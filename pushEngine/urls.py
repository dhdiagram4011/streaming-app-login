from django.urls import path
from searchEngine import views
from .views import *


urlpatterns = [
    path('send/', MsgSend, name='MsgSend'),
    # path('sendList/', sendList, name=sendList),
    # path('revList/', revList, name=revList),
]
