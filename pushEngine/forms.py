from .models import MsgPush


class MsgPushForm(forms.ModelForm):
    class Meta:
        model = MsgPush
        fields = ['sender','receiver','title','text'] 
        
    sender = forms.CharField(max_length=13)
    receiver = forms.CharField(max_length=13)
    title = forms.CharField(max_length=100)
    text = forms.CharField(max_length=500)



