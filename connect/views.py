from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from connect.forms import UserForm
# from connect.forms import ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from forum.models import *


# Create your views here.
# Views for connex page.
def index(request):

    return render(request,'index.html')
def connexion(request):
    return render(request,'connect/connexion.html')

@login_required(login_url='/user_login/')
def my_account(request):
    current_user = request.user
    query_1 = list(Quest_ans.objects.filter(user_h=current_user).values())
    return render(request,'connect/my_account.html', {'query_1':query_1})
@login_required
def special(request):
    return HttpResponse("You are logged in !")
# Views for deconnect user.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
# Views for register user.
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            messages.success(request, ('Votre profil a été enregistré!'))
            return HttpResponseRedirect(reverse('user_login'))   
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        
       
    return render(request,'connect/registration.html',
                          {'user_form':user_form,
                           'registered':registered})
# Views for connect user.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".
                    format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'connect/login.html', {})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'connect/change_password.html', {
        'form': form
    })
