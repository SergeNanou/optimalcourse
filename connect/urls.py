from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^password/$', views.change_password,
        name='change_password'),
    
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^connexion/$', views.connexion, name='connexion'),
    url(r'^user_logout/$', views.user_logout, name='logout'),
    url(r'^my_account/$', views.my_account, name='my_account'),
]
