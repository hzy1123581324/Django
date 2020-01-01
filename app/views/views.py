from django.shortcuts import HttpResponse,redirect,render


# Create your views here.


def login(request):
  #  return render(request,"login.html")
  return HttpResponse('你好')
  # return redirect('/index/');

def index(request):
  COOKIES = request.COOKIES
  SESSION = request.session
  username =  request.GET.get('username')
  # print(username)
  data ='COOKIES:%s,SESSION:%s,'%(COOKIES,SESSION)
  return HttpResponse(data)
  # return render(request,"index.html")




