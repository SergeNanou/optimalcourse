from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^teach/$', views.teach, name='teach'),
    url(r'^test_level/$', views.TestLevel, name='test_level'),
    
]
