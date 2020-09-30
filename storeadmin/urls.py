"""adsense URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.conf.urls import url,include
from django.urls import path, re_path,include
from django.contrib import admin
from storeadmin import views
urlpatterns = [

    re_path('^$', views.app_index, name="app_index"),
	
    path('/demo',views.test,name = 'test'),
    path('/scroll',views.scroll,name = 'scroll'),
	re_path('err/(\d+)$', views.err,name="err"),
	
    # url(r'^(\w+)/(\w+)/$', views.table_obj_list, name="table_obj_list"),
    # url(r'^(\w+)/(\w+)/(\d+)/change/$', views.table_obj_change, name="table_obj_change"),
    # url(r'^(\w+)/(\w+)/add/$', views.table_obj_add, name="table_obj_add"),
    # url(r'^(\w+)/(\w+)/(\d+)/delete/$', views.table_obj_delete, name="obj_delete"),

    # url(r'^login/',views.acc_login ),
    # url(r'^logout/',views.acc_logout,name="logout" ),


]