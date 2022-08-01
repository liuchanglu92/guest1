#Django的视图文件，控制箱前端页面显示的内容
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request,"index.html")
def login_action(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        #if username=='admin' and password=='admin123':
        if user is not None:
            auth.login(request,user)
            request.session['user']=username
            response= HttpResponseRedirect('/event_manage/')
            #response.set_cookie('user',username,3600) #添加浏览器cookie
            request.session['user']=username  #将session信息记录到浏览器
            return response
        else:
            return render(request,'index.html',{'error':'username or password error！'})
@login_required #防止未登录访问页面
def event_manage(request):
    #username=request.COOKIES.get('user','') #读取浏览器cookie
    username=request.session.get('user','')
    return  render(request,'event_manage.html',{'user':username})