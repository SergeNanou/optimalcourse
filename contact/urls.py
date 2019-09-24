from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^legal/$', views.legal, name='legal'),
]
