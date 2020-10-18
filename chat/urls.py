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
# from django.contrib import admin
# # from django.conf.urls import url
# from django.urls import include
from . import views
from django.urls import re_path
from django.urls import path, re_path
# from blockchain import views as b_biew
# from app.views import views,login
# from django.conf import settings
# from django.conf.urls.static import static

# from django.views import static ##新增
# from django.conf import settings ##新增
# from django.conf.urls import url ##新增


# 增加的条目
# handler400 = views.bad_request
# handler403 = views.permission_denied
# handler404 = views.page_not_found
# handler500 = views.page_error

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # re_path('^mine', b_biew.mine, name="blockMine"),
    # re_path('^transactions/new/', b_biew.new_transaction, name="blockNew"),
    # re_path('^chain/', b_biew.full_chain, name="blockChain"),
    # re_path('^register', b_biew.register_nodes, name="blockRegister"),
    # re_path('^resolve', b_biew.consensus, name="blockRresolve"),


]


# urlpatterns = [
#     re_path(r'^$', views.index, name='index'),
#     re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
# ]
