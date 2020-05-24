from django.shortcuts import HttpResponse,redirect,render
# from django.db.models import Avg,Min,Sum,Max,Count
# from django.db.models import Q,F
from app.models.models import User
from app.models.goodModels import *

# Create your views here.


# def login(request):
#   #  return render(request,"login.html")
#   user =  User.objects.filter(name="人民出版社")[0]
#   return HttpResponse('你好')
#   # return redirect('/index/');

def index(request):
  COOKIES = request.COOKIES
  SESSION = request.session
  # username =  request.GET.get('username')
  # print(username)
  data ='COOKIES:%s,SESSION:%s,'%(COOKIES,SESSION)
#   return HttpResponse(data)
  return render(request,"index.html")

def getdata(request):
    print('888888888888888888888888888888')
    print(User,':::::::::::::::')
    user = User.objects.all().values()
    return HttpResponse(user)


def updated(request):
    print(request.POST)
    print(request.FILES)
    print(request.FILES.get('tt',None))

    return HttpResponse('999999')

def download(request):
    filename = request.GET.get('file')
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    fp = open(filepath, 'rb')
    response = StreamingHttpResponse(fp)
    # response = FileResponse(fp)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s"' % filename
    return response
    fp.close()






























# 异常处理
def page_not_found(request,exception,template_name='404.html'):
    return render(request, 'test.html')


def page_error(request,template_name='500.html'):
    return render(request, template_name)


def permission_denied(request,exception,template_name='403.html'):
    return render(request, template_name)


def bad_request(request,exception,template_name='400.html'):
    return render(request, template_name)
