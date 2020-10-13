from django.urls import path
from searchEngine import views


urlpattenrs = [
    path('send/', send, name=send),
    path('sendList/', sendList, name=sendList),
    path('revList/', revList, name=revList),
]