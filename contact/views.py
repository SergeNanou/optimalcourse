from django.shortcuts import render
from contact.forms import *
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .models import ContLead


# views create for legal mentions page.
def legal(request):
	return render(request, 'legal_ment.html')

# views create for contact form
def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            yourname = form.cleaned_data['yourname']
            sujet = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            
            ContLead.objects.create(yourname=yourname,
                                    subject=sujet,
                                    message=message,
                                    email=email)
            # assert False
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:             
        	submitted = True
    return render(request, 'contact/contact.html', {'form': form, 'submitted': submitted})