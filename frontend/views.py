import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth

@login_required(login_url='/login/')
def index(request):
    return render(request, 'index.html')


@login_required(login_url='/login/')
def js(request, filename):
    file_path = os.path.join(settings.BASE_DIR, "frontend", "js", filename)
    print("Load js", file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/javascript")
            return response

    raise Http404


def login(request):
    return render(request, 'login.html')


def login_submit(request):
    #if this user is authenticated, send the user to main page
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    username = request.POST.get('username','N')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        errorMsg = "Login Failure!"
        return render(request,'login.html',locals())


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')