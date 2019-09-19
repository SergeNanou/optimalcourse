
from django import forms

from django.contrib.auth.models import User


# form model to create accou
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),
    	                       help_text='Required. Enter a valid password')
    class Meta():
        model = User
        fields = ('username', 'password', 'email')
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('status', 'location', 'biography')