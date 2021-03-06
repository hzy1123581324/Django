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
from django.contrib import admin
# from django.conf.urls import url
from django.urls import include
from django.urls import path, re_path
from web.views import views as web_views
from app.views import views, login
from django.conf import settings
from django.conf.urls.static import static

from django.views import static  # 新增
from django.conf import settings  # 新增
from django.conf.urls import url  # 新增


# 增加的条目
handler400 = views.bad_request
handler403 = views.permission_denied
handler404 = views.page_not_found
handler500 = views.page_error

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^static/(?P<path>.*)$', static.serve,
    #     {'document_root': settings.STATIC_ROOT}, name='static'),



    path('', views.index),
    re_path('^storeadmin', include('storeadmin.urls')),
    re_path('^kingadmin', include('kingadmin.urls')),
    re_path('^store', include('store.urls')),
    re_path('^blockchain', include('blockchain.urls')),
    re_path('^chat', include('chat.urls')),
    path('index/', views.index),
    re_path('^page/.html$', web_views.index),
    path('test/', web_views.index),
    path('getdata', views.getdata),
    path('updated', views.updated),
    re_path('^login/', login.LoginView.as_view()),
    # re_path('^page/(?P<page>\w+).html?(?P<>)', views.detail, name="detail",)


]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)

#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
