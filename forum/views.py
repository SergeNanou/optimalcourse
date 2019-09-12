from django.shortcuts import render
from forum.forms import MessageForm
from forum.models import Message
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




