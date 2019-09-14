from django import forms

class MessageForm(forms.Form):
    
    message = forms.CharField(widget=forms.Textarea, help_text='*')
    sujet = forms.CharField(help_text='*')
    email = forms.EmailField(help_text='*')
    phone = forms.IntegerField(help_text='*')

class HelpForm(forms.Form):
	message = forms.CharField(widget=forms.Textarea, help_text='*')
	sujet = forms.CharField(help_text='*')
	email = forms.EmailField(help_text='*')
	phone = forms.IntegerField(help_text='*')


    