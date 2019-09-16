from django.shortcuts import render

# Create your views here.
def study(request):
    return render(request, 'study/study_ac.html')

def coaching(request):
    return render(request, 'study/coaching.html')

def stage(request):
    return render(request, 'study/stage.html')

def prepas(request):
    return render(request, 'study/prepas.html')