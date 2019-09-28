from django.shortcuts import render
from teach.forms import TeachForm, StudentForm
from teach.models import Curriculum, StudentTest

# Create your views here.
def teach(request):
    sauvegarde = False
    form = TeachForm(request.POST or None, request.FILES)
    if form.is_valid():
        curriculum = Curriculum()
        curriculum.teach_cv = form.cleaned_data["teach_cv"]
        curriculum.save()
        sauvegarde = True

    return render(request, 'teach/ind_teach.html', {
        'form': form, 
        'sauvegarde': sauvegarde
    })

	
def TestLevel(request):
    # variable initiliazation
    sauvegarde = False
    form = StudentForm(request.POST or None)
    # if this is a POST request we need to process the form data
    
    # create a form instance and populate it with data from the request:
        
    # check whether it's valid:
    if form.is_valid():
        sauvegarde = True
        niveau = form.cleaned_data['niveau']
        matiere = form.cleaned_data['matiere']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        StudentTest.objects.create(level=niveau,
                                   study=matiere,
                                   email=email,
                                   phone=phone)
    return render(request,'teach/lev_test.html', {'form': form, 
        	'sauvegarde':sauvegarde})
