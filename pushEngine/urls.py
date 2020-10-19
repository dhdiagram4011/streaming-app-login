from django.urls import path
from searchEngine import views


urlpattenrs = [
    path('send/', MsgSend, name=MsgSend),
    path('sendList/', sendList, name=sendList),
    path('revList/', revList, name=revList),
]

