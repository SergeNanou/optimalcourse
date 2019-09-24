from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^study/$', views.study, 
        name='study'),
    url(r'^coaching/$', views.coaching, name='coaching'),
    url(r'^stage/$', views.stage, name='stage'),
    url(r'^prepas/$', views.prepas, name='prepas'),
]
