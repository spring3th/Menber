from django.template import loader,Context,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from menber.models import Menbers,MyUser
from django.contrib import auth
from django.shortcuts import render_to_response,render
from django.contrib.auth.models import User

# Create your views here.

def Menber(request):
    menber = Menbers.objects.all()
    t = loader.get_template('menber.html')
    c = Context({'menber':menber})
    return HttpResponse(t.render(c))

def Index(request):
    return render_to_response("index.html",{})

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
         q = request.GET['q']
         menber = Menbers.objects.filter(menber_name=q)
         return render_to_response('search_result.html',
                                   {'menber':menber,'query':q})
    else:
        return render_to_response('search_form.html',{'error':True})

def signup(req):
    if req.session.get('username',''):
        return HttpResponseRedirect('/')
    status = ''
    if  req.POST:
        post = req.POST
        passwd = post.get('passwd','')
        repasswd = post.get('repasswd','')
        if passwd != repasswd: 
            status = 're_err'
        else:
            username = post.get('username','')
            if User.objects.filter(username=username):
                status = 'user_exist'
            else:
                newuser = User.objects.create_user(username=username,passwd=passwd,email=post.get('email',''))
                newuser.save()
                new_myuser = MyUser(user=newuser,nickname=post.get('nickname'),permission=1)
                new_myuser.save()
                status = 'success'
    content = {'active_menu':'homepage','status':status,'user':''}
    return render_to_response('signup.html',content,context_instance=RequestContext(req))
