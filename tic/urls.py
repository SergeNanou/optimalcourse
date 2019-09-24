from . import views
from django.conf.urls import url, include

urlpatterns = [
    
    url(r'^tic/$', views.tic, name='tic'),
]




