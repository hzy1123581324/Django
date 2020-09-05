# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django import conf
import json
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# from kingadmin import app_setup
# from kingadmin import form_handle
# app_setup.kingadmin_auto_discover()


# from kingadmin.sites import  site
# print("sites.",site.enabled_admins)

def app_index(request):
    #enabled_admins =
    return HttpResponseRedirect('/storeadmin/err/404')
    # return render(request,'storeadmin/app_index.html', {'site':'site',})
	
def err(request,code):
    #enabled_admins =
    # print(request,'这个是')
    return render(request,'err.html',{'code':code})