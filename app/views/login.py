from django.shortcuts import HttpResponse,redirect,render
# from django import views
from django.views.generic import ListView
# Create your views here.

# 检查登录
def Check_Login(func):  #自定义登录验证装饰器
    def warpper(request,*args,**kwargs):
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/polls/login_user")
    return warpper



class LoginView(ListView):

  def get(self, request):
    # <view logic>
    import time
    time.sleep(10)
    
    return HttpResponse('55555555555555555')

  def post(self,request):
    return HttpResponse('66666666')

class register(ListView):
  pass


