from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text',)
        widgets = {
            'text': forms.TextInput(attrs={'class': "mdl-textfield__input"}),
        }
        labels = {
            'text': 'Send Me Messages'
        }
