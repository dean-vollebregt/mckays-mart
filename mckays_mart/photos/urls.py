from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^bathroom/$', views.bathroom_list, name='bathroom_list'),
    url(r'^bedroom/$', views.bedroom_list, name='bedroom_list'),
    url(r'^dining/$', views.dining_list, name='dining_list'),
    url(r'^hallway/$', views.hallway_list, name='hallway_list'),
    url(r'^living/$', views.living_list, name='living_list'),
    url(r'^office/$', views.office_list, name='office_list'),
    url(r'^musical/$', views.musical_list, name='musical_list'),
    url(r'^art/$', views.art_list, name='art_list'),
]
