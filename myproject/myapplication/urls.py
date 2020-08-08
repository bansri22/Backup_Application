from django.urls import re_path
from . import views

#this page shows the path for different page with which method must call
urlpatterns = [
    re_path(r'^$', views.show, name='home'),
    re_path(r'^show', views.index, name='show'),
    re_path(r'^home', views.show, name='home'),
    re_path(r'^search', views.search, name='search'),
    re_path(r'^delete', views.delete, name='delete'),

]
