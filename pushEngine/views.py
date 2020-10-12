from django.shortcuts import render
from .models import MsgPush

#### urlconf List
# path('send/', send, name=send),
# path('sendList/', sendList, name=sendList),
# path('revList/', revList, name=revList),


def send(request):
    if request.method == 'GET':
        ### action
        form = sendForm(request.GET)
        return render(request, 'pushEngine/send.html', {'form':form})
    elif request.method == 'POST':
        form = sendForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            ### model field save() : send, receiver, title , text
            send = request.POST['send']
            receiver = request.POST['receiver']
            title = request.POST['title']
            text = request.POST['text']
            post.save()
        return render(request, 'pushEngine/send_success.html')
        


def sendList(request):
    if request.method == 'POST':
        form = sendListForm(request.POST)    
        ### action

    else:



def revList(request):
    if request.method == 'POST':
        form = revListForm(request.POST)
        ### action
    else:


