from django.shortcuts import render
from blog.models import *


# Create a  view to publish extract article.
def edit(request):
    publish = list(Article.objects.all().order_by('-date').values())
    publish = publish[0]
    publish['photo'] = '/media/'+publish['photo']
    return render(request, 'blog/base.html', {'publish': publish})
