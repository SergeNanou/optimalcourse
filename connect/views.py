from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from connect.forms import UserForm
from connect.forms import ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
# Views for connex page.
def index(request):

    return render(request,'index.html')
def connexion(request):
    return render(request,'connect/connexion.html')

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

