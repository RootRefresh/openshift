#coding:utf8
from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    return render(request,'home.html')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def old_add_redirect(request,a,b):
    return HttpResponseRedirect(
        reverse('add2',args=(a,b))
    )

def add2(request,a,b):
    c = int(a)+int(b)
    return HttpResponse(str(c))