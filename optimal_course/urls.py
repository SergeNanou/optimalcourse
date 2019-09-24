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
import teach
import study
import blog
import contact
from connect import views
from tic import views
from forum import views
from teach import views
from study import views
from blog import views
from contact import views
from . import  settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', include('forum.urls')),
    path('connect/', include('connect.urls')),
    path('contact/', include('contact.urls')),
    path('study/', include('study.urls')),
    path('teach/', include('teach.urls')),
    path('tic/', include('tic.urls')),
    path('blog/', include('blog.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)