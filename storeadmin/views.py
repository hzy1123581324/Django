# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import conf
import json
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from kingadmin import app_setup
# from kingadmin import form_handle
# app_setup.kingadmin_auto_discover()


# from kingadmin.sites import  site
# print("sites.",site.enabled_admins)

def app_index(request):
    # enabled_admins =
    # return HttpResponseRedirect('/storeadmin/err/404')
    sideList = [
        {
            'child': [],
            'title': '标题1',
            'url': '#',
            "id": 1
        },
        {
            "id": 2,
            'child': [
                {
                    'title': '标题2-1',
                    'url': '#',
                    "id": "2-1"
                },
                {
                    'title': '标题2-2',
                    'url': '#',
                    "id": "2-0"
                },
                {
                    'title': '标题2-3',
                    'url': '#',
                    "id": "2-2"
                },
                {
                    'title': '标题2-4',
                    'url': '#',
                    "id": "2-3"
                },
                {
                    'title': '标题2-4',
                    'url': '#',
                    "id": "2-4"
                },

            ],
            'title': '标题2',
        },
        {
            "id": "3",
            'child': [
                {
                    'title': '标题3-1',
                    'url': '#',
                    "id": "3-2"
                },
                {
                    'title': '标题3-2',
                    'url': '#',
                    "id": "3-1"
                },
            ],
            'title': '标题3'
        },
    ]
    # sideList = [{},{}]
    print(json.dumps(sideList))
    return render(request, 'storeadmin/index.html', {'site': 'site', 'sideList': str(sideList).encode('utf-8').decode("utf-8")})


def scroll(request):
    return render(request, 'storeadmin/scroll.html')


def test(request):
    return render(request, 'storeadmin/demo.html')


def err(request, code):
    # enabled_admins =
    # print(request,'这个是')
    return render(request, 'err.html', {'code': code, 'message': '页面找不到了'})
