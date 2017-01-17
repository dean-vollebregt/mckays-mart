from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^hours/$', views.hours, name='hours'),

]
