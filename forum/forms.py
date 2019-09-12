from django import forms

class MessageForm(forms.Form):
    
    message = forms.CharField(widget=forms.Textarea, help_text='champs requis')
    sujet = forms.CharField(help_text='champs requis')
    email = forms.EmailField(help_text='champs requis')
    phone = forms.IntegerField(help_text='champs requis')
    