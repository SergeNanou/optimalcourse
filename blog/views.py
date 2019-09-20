from django.shortcuts import render

# Create your views here.
def edit(request):
	return render(request, 'blog/base.html')
