from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^edit/$',views.edit, name='edit'),
]