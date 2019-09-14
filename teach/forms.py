from django import forms

class TeachForm(forms.Form):
    
    teach_cv = forms.FileField()