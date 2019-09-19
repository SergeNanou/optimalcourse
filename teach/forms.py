from django import forms

class TeachForm(forms.Form):
    
    teach_cv = forms.FileField()

class StudentForm(forms.Form):
    niveau = forms.CharField(help_text='*')
    matiere = forms.CharField(help_text='*')
    email = forms.EmailField(help_text='*')
    phone = forms.IntegerField(help_text='*')
