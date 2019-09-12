"""optimal_course URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
import connect
import tic
import forum
from connect import views
from tic import views
from forum import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', connect.views.index, name='index'),
    url(r'^register/$', connect.views.register, name='register'),
    url(r'^user_login/$', connect.views.user_login, name='user_login'),
    url(r'^connexion/$', connect.views.connexion, name='connexion'),
    url(r'^user_logout/$', connect.views.user_logout, name='logout'),
    url(r'^tic/$', tic.views.tic, name='tic'),
    url(r'^publish/$', forum.views.publish, name='publish'),
    url(r'^read/$', forum.views.read, name='read'),

]
