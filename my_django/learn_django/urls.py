from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^add/$', add),
    url(r'^add/(\d+)/(\d+)/$', old_add_redirect),
    url(r'^new_add/(\d+)/(\d+)/$', add2, name='add2'),
]