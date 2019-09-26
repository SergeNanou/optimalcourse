from django.shortcuts import render
from blog.models import *


# Create a  view to publish extract article.
def edit(request):
    publish = list(Article.objects.all().order_by('-date').values())
    publish = publish[0]
    publish['photo'] = '/media/'+publish['photo']
    return render(request, 'blog/base.html', {'publish': publish})
# Create a  view to publish extract article.
def read(request):
    publish = list(Article.objects.all().order_by('-date').values())
    for pub in publish:
        pub['photo'] = '/media/'+pub['photo']
        pub['contenu'] = pub['contenu'][0:225]

    return render(request, 'blog/base_1.html', {'publish': publish})
