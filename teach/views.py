from django.shortcuts import render
from teach.forms import TeachForm
from teach.models import Curriculum

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
