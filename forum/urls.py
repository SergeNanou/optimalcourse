from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^help_ent/$', views.help_ent, name='help_ent'),
    url(r'^help_ent_publish/$', views.help_ent_publish, 
        name='help_ent_publish'),
    url(r'^help_ent_ans/$', views.help_ent_ans, 
        name='help_ent_ans'),
    url(r'^read_ans/$', views.read_ans, name='read_ans'),
]
