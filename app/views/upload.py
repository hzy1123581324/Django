from django.http import HttpResponseRedirect
from django.shortcuts import render
from app.forms import UploadFileForm

# 另外写一个处理上传过来的文件的方法，并在这里导入
from somewhere import handle_uploaded_file

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES) # 注意获取数据的方式
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


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

def upload(request):
    if request.method == "POST":  # 请求方法为POST时，进行处理
    myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
    if not myFile:
        return HttpResponse("no files for upload!")
    # destination=open(os.path.join('upload',myFile.name),'wb+')
    destination = open(
        os.path.join("你的文件存放地址", myFile.name),
        'wb+')  # 打开特定的文件进行二进制的写操作
    for chunk in myFile.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()
    return HttpResponse("upload over!")
else:
    file_list = []
    files = os.listdir('D:\python\Salary management system\django\managementsystem\\file')
    for i in files:
        file_list.append(i)
    return render(request, 'upload.html', {'file_list': file_list})
