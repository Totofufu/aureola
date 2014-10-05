from django.conf.urls import patterns, include, url
from api import views

urlpatterns = patterns('',
    url(r'suportees$', views.GetSuportees.as_view())
)