from django.shortcuts import HttpResponse,redirect,render
# from django import views
from django.views.generic import ListView
# Create your views here.

class LoginView(ListView):

  def get(self, request):
    # <view logic>
    import time
    time.sleep(10)
    
    return HttpResponse('55555555555555555')

  def post(self,request):
    return HttpResponse('66666666')

