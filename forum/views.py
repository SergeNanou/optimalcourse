from django.shortcuts import render
from forum.forms import MessageForm, HelpForm
from forum.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
# create a view to publish in forum
@login_required(login_url='/user_login/')
def publish(request):
    # variable initiliazation
    current_user = request.user
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MessageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            Message.objects.create(user=current_user,
                                   sujet=sujet,
                                   message=message,
                                   email=email,
                                   phone=phone)
            return HttpResponse(message)

        # if a GET (or any other method) we'll create a blank form
    else:
        form = MessageForm()

    

    return render(request,'forum/ind_tic.html', {'form': form})

# create to read in forum
def read(request):

    # take  all messages publishing
    publish = list(Message.objects.all().order_by ('-created_at__date').values())
    # for tim in publish:
    #     tim.created_at = tim.created_at.isoformat()

    return render(request,'forum/ind_tic_r.html', {'publish':publish})

@login_required(login_url='/user_login/')
def help_ent(request):
    return render(request,'forum/help_ent.html')

@login_required(login_url='/user_login/')
def help_ent_publish(request):
    # variable initiliazation
    sauvegarde = False
    current_user = request.user
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = HelpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            save = True
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            Quest_ans.objects.create(user_h=current_user,
                                     sujet_h=sujet,
                                     message_h=message,
                                     email_h=email,
                                     phone_h=phone)
        return render(request,'forum/help_ent.html', {sauvegarde:'sauvegarde'})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = HelpForm()
    return render(request,'forum/for_ent_pub.html', {'form': form})




