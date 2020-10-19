from django.shortcuts import render
from .models import MsgPush

#### urlconf List
# path('send/', send, name=send),
# path('sendList/', sendList, name=sendList),
# path('revList/', revList, name=revList),

### forms.py
# model = MsgPush
#         fields = ['sender','receiver','title','text'] 
        
#     sender = forms.CharField(max_length=13)
#     receiver = forms.CharField(max_length=13)
#     title = forms.CharField(max_length=100)
#     text = forms.CharField(max_length=500)


def MsgSend(request):
    if request.method == 'GET':
        form = MsgPushForm(request.GET)
        return render(request, 'pushEngine/send.html', {'form':form})
    elif request.method == 'POST':
        form = sendForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            send = request.POST['send']
            receiver = request.POST['receiver']
            title = request.POST['title']
            text = request.POST['text']
            post.save()
        return render(request, 'pushEngine/send_success.html')
