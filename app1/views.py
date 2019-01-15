from django.shortcuts import render
from  .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .models import *
from datetime import datetime
from django.http import HttpResponse, HttpResponseForbidden


def index(request):
    if request.user.is_authenticated == False:
        return HttpResponseRedirect("login/1")
    if request.method == "POST":
        dep_pnt = request.POST.get("dep")
        arr_pnt = request.POST.get("arr")
        dep_tme = request.POST.get("ddt")
        flgts = Flight.objects.all()
        if dep_pnt != "":
            flgts = flgts.filter(dep_point=dep_pnt)
        if arr_pnt != "":
            flgts = flgts.filter(arr_point=arr_pnt)
        if dep_tme != "":
            dep_tme = datetime.strptime(dep_tme, "%Y-%m-%d").date()
            flgts = flgts.filter(dep_time=dep_tme)
        if flgts.__len__() == 0:
            log = "Ничего не нашлось"
            return render(request, "index.html", {"form": SearchForm(), "log": log, "prof": request.user.username})
        return render(request, "index.html", {"data": flgts, "prof": request.user.username})
    else:
        userform = SearchForm()
        return render(request, "index.html", {"form": userform, "user": request.user})


def log_out(request):
    logout(request)
    return HttpResponseRedirect("login/2")


def login(request, log=""):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    if (log != ''):
        logs = ["Сперва авторизиуйтесь","Вы успешно вышли"]
        log = logs[int(log) - 1]
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("login")
        else:
            log = "Введена не правильная пара логин-пароль"
    userform = LoginForm()
    return render(request, "login.html", {"form": userform, "log": log})


def regist(request, log=""):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    if (log != ''):
        logs = ["Имя пользователя используется","Email используется"]
        log = logs[int(log) - 1]
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        checkuser = User.objects.filter(username=username)
        if (checkuser.__len__() > 0):
            return HttpResponseRedirect("/reg/1")
        checkuser = User.objects.filter(email=email)
        if (checkuser.__len__() > 0):
            return HttpResponseRedirect("/reg/2")
        user = UserFly.create(username, email, password)
        auth_login(request,user)
        return HttpResponseRedirect("profile")
    else:
        userform = RegistrForm()
        return render(request, "registration.html", {"form": userform, "log": log})


def prof(request):
    if request.user.is_authenticated == False:
        return HttpResponseRedirect("/")
    if request.method == "POST":
        flag = False
        firstname = "" + request.POST.get("firstname")
        lastname = "" + request.POST.get("lastname")
        email = "" + request.POST.get("email")
        about = "" + request.POST.get("about")
        user = UserFly.transform(request.user)
        if (firstname != "") & (firstname != user.first_name):
            flag = True
            user.first_name = firstname
        if (lastname != "") & (lastname != user.last_name):
            flag = True
            user.last_name = lastname
        if (email != "") & (email != user.email):
            flag = True
            user.email = email
        if (about != "") & (about != user.get_info()):
            flag = True
            user.set_info(about)
        if flag:
            user.save()
        return HttpResponseRedirect("/prof")
    else:
        userform = ProfForm()
        user = UserFly.transform(request.user)
        return render(request, "profile.html", {"form": userform, "user": request.user, "get_info": user.get_info()})


def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = ExampleModel.objects.create(model_pic=form.image)
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')