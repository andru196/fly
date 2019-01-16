from django.shortcuts import render, render_to_response
from  .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout
from django.http import HttpResponseRedirect
from .models import *
from django.http import HttpResponse, HttpResponseForbidden
import json
import datetime


#Проверь все!!!!!, удали коменты
def index(request):
    if request.user.is_authenticated == False:
        return HttpResponseRedirect("login/1")
    """if request.method == "POST":
        dep_pnt = request.POST.get("dep")
        arr_pnt = request.POST.get("arr")
        dep_tme = request.POST.get("ddt")
        flgts = Flight.objects.all()
        if dep_pnt != "":
            flgts = flgts.filter(dep_point=dep_pnt)
        if arr_pnt != "":
            flgts = flgts.filter(arr_point=arr_pnt)
        #if dep_tme != "": #Тут не успел починить
        #    dep_tme = datetime.strptime(dep_tme, "%Y-%m-%d").date()
        #    flgts = flgts.filter(dep_time=dep_tme)
        if flgts.__len__() == 0:
            log = "Ничего не нашлось"
            return render(request, "index.html", {"form": SearchForm(), "log": log, "prof": request.user.username})
        return render(request, "index.html", {"data": flgts, "user": request.user, }) #Тут что-то придется переделать под айакс
    else:"""                                                                             #в основном в шаблоне, но и здесь
    userform = SearchForm()                                                       #может функцию добавить
    return render(request, "index.html", {"form": userform, "user": request.user})


###############################################
#AJAX#AJAX#AJAX#AJAX#AJAX#AJAX#AJAX#AJAX#AJAX##
###############################################

def returner_flights(flights):
    arr = []
    i = 0
    for el in flights:
        arr.append({"from": el.dep_point, "to": el.arr_point, "time": str(el.dep_time), "time2": str(el.arr_time)})
    return json.dumps(arr)


def returner_indexes(flights):
    arr = []
    i = 0
    for el in flights:
        arr.append(el.id)
    return json.dumps(arr)


def search(request):
    dep_pnt = request.GET.get("dep")
    arr_pnt = request.GET.get("arr")
    dep_time = request.GET.get("ddt")
    id1 = request.GET.get("id1")
    if id1 != None:
        id1 = int(id1)
        if id1 != 0:
            rez = Flight.objects.get(id=id1)
        return HttpResponse(returner_flights((rez,)))
    flgts = Flight.objects.all()
    if dep_pnt != "":
        flgts = flgts.filter(dep_point=dep_pnt)
    if arr_pnt != "":
        flgts = flgts.filter(arr_point=arr_pnt)
    #if dep_time != "": #Тут не успел починить
    #    dep_time = datetime.strptime(dep_time, "%Y-%m-%d")
    #    flgts = flgts.filter(dep_time__mt=dep_time)
    return HttpResponse(returner_indexes(flgts))


def add_f(request):
    dep_pnt = request.GET.get("dep")
    arr_pnt = request.GET.get("arr")
    dep_time = request.GET.get("dep_time")
    arr_time = request.GET.get("arr_time")
    fl = Flight.objects.create(dep_time=dep_time, arr_time=arr_time, dep_point=dep_pnt, arr_point=arr_pnt)
    fl.save()
    return HttpResponse(fl)

###############################################
#AJAX#AJAX#AJAX#AJAX#AJAX#AJAX#AJAX#AJAX#AJAX##
###############################################


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

#Тут надо на айаксе проверить доступглсть логина/пароля
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

#тут всё плохо, надо как-то фото прикрутить
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

#Тут корявенько, но работает
def add_my_ticket(request):
    log = ""
    if request.method == "POST":
        if request.POST.get("cost") != None:
            cost = request.POST.get("cost")
            flight = Flight.objects.get(id=request.POST.get("flight"))
            tick = Ticket.objects.create(cost=cost, flight=flight, owner=request.user)
            tick.save()
        elif request.POST.get("dep_time") != None:
            dep_time = request.POST.get("dep_time")
            arr_time = request.POST.get("arr_time")
            dep_point = request.POST.get("dep_point")
            arr_point = request.POST.get("arr_point")
            fl = Flight.objects.create(dep_time=dep_time, arr_time=arr_time,dep_point=dep_point,arr_point=arr_point)
            fl.save()
    userform = FormTAdd()
    form0 = FormFAdd()
    return render(request, "add_my.html", {"form": userform, "form0": form0, "log": log})

#Можно как-то объеденить с функцией выше
def my_tick(request):
    data = Ticket.objects.filter(owner=request.user)
    len = data.__len__()
    return render(request, "my_tick.html", {"data": data,"len": len})

#Это гавно не заработало
def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = ExampleModel.objects.create(model_pic=form.image)
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')