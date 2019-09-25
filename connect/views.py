from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from connect.forms import UserForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.forms import PasswordChangeForm
from forum.models import *
from blog.models import *


# Create your views here.
# Views for connex page.
def index(request):
    publis = list(Article.objects.all().values())
    publish = publis[0]['photo']
    publish = '/media/'+publish
    contenu = publis[0]['contenu']
    text = contenu[0:225]
    titre = publis[0]['titre']
    return render(request,'index.html',{'publish':publish,
                                        'contenu':contenu, 
                                        'titre':titre,
                                        'text':text})
def connexion(request):
    return render(request,'connect/connexion.html')

@login_required(login_url='/user_login/')
def my_account(request):
    current_user = request.user
    query_1 = list(Quest_ans.objects.filter(user_h=current_user).values())
    # Slice pages
    paginator = Paginator(query_1, 4)
    # Get current page number
    page = request.GET.get('page')
    try:
        # Return only this page albums and not others
        query_1 = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query_1 = paginator.page(1)
    except EmptyPage:
        # If page is out of range,
        # deliver last page of results.
        query_1 = paginator.page(paginator.num_pages)
    return render(request,'connect/my_account.html', {'query_1':query_1})

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

# Views for change password
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
