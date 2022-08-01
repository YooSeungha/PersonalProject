import logging

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .models import Address
from .models import Board
from .models import Member
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login


#def index(request):
    # return HttpResponse("안녕장고")

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({},request))
# 주소록
from django.db.models import Q
def list(request):
    template = loader.get_template('list.html')
    addresses = Address.objects.all().values()
    context = {
        'addresses': addresses,
    }
    return HttpResponse(template.render(context, request))


def write(request):
    template = loader.get_template('write.html')
    return HttpResponse(template.render({}, request))

from django.urls import reverse
from django.utils import timezone
def write_ok(request):
    x = request.POST['name']
    y = request.POST['addr']
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    address = Address(name=x, addr=y, rdate=nowDatetime)
    address.save()
    return HttpResponseRedirect(reverse('list'))


def delete(request, id):
    address = Address.objects.get(id=id)
    address.delete()
    return HttpResponseRedirect(reverse('list'))


def update(request, id):
    template = loader.get_template('update.html')
    address = Address.objects.get(id=id)
    context = {
        'address': address,
    }
    return HttpResponse(template.render(context, request))


def update_ok(request, id):
    x = request.POST['name']
    y = request.POST['addr']
    address = Address.objects.get(id=id)
    address.name = x
    address.addr = y
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')  # 옵션
    address.rdate = nowDatetime  # 옵션
    address.save()
    return HttpResponseRedirect(reverse('list'))
# 게시판
def b_list(request):
    template = loader.get_template('b_list.html')
    boards = Board.objects.all().values()
    page = request.GET.get('page','1')
    paginator = Paginator(boards, 5)
    page_obj = paginator.get_page(page)
    context = {
        #'boards': boards,
        'boards' : page_obj
    }

    return HttpResponse(template.render(context, request))

def b_write(request):
    template = loader.get_template('b_write.html')
    return HttpResponse(template.render({}, request))

def b_write_ok(request):
    x = request.POST['writer']
    y = request.POST['email']
    c = request.POST['subject']
    d = request.POST['content']
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    board = Board(writer=x, email=y, subject=c,content=d, rdate=nowDatetime)
    board.save()
    return HttpResponseRedirect(reverse('b_list'))

def b_content(request, id):
    template = loader.get_template('b_content.html')
    board = Board.objects.get(id=id)
    context = {
        'board': board,
    }
    return HttpResponse(template.render(context, request))

def b_delete(request, id):
    board = Board.objects.get(id=id)
    board.delete()
    return HttpResponseRedirect(reverse('b_list'))

def b_update(request, id):
    template = loader.get_template('b_update.html')
    board = Board.objects.get(id=id)
    context = {
        'board': board,
    }
    return HttpResponse(template.render(context, request))

def b_update_ok(request, id):
    b = request.POST['email']
    c = request.POST['subject']
    d = request.POST['content']
    board = Board.objects.get(id=id)
    board.email = b
    board.subject = c
    board.content = d
    board.save()
    return HttpResponseRedirect(reverse('b_list'))
# 로그인
def login(request):
    return render(request, 'login.html')

def login_ok(request):
    email = request.POST.get('email',None)
    pwd = request.POST.get('pwd',None)

    try:
        member = Member.objects.get(email=email)
    except Member.DoesNotExist:
        member = None
    result = 0
    if member != None:
        if member.pwd == pwd:
            result = 2
            request.session['login_ok_user'] = 'member.email'
        else:
            result = 1
    else:
        result = 0
    template = loader.get_template("login_ok.html")
    context = {
        'result': result,
    }
    return HttpResponse(template.render(context, request))

def logout(request):
    if request.session.get('login_ok_user'):
        del request.session['login_ok_user']
        #request.session.clear()
        #request.session.flush()
    return redirect("../")

# 템플릿
def test1(request):
    addresses = Address.objects.all().values()
    template = loader.get_template("template1.html")
    context ={
        'yourname': '길동',
        'addresses': addresses,
    }
    return HttpResponse(template.render(context,request))

def test2(request):
    template = loader.get_template('template2.html')
    context = {
        'x' : 2,
        'y' : 'tiger',
        'fruits1' : ['apple','orange','banana','melon'],
        'z': 'tiger',
        'fruits2': ['apple', 'orange', 'banana', 'melon'],
    }
    return HttpResponse(template.render(context,request))

def test3(request):
    template = loader.get_template('template3.html')
    addresses = Address.objects.all().values()
    context = {
        'fruits': ['apple', 'orange', 'banana', 'melon'],
        'cars': [{'brand': '현대', 'model':'소나타','year':'2022'},
                 {'brand': '테슬라', 'model':'모델x','year':'2020'}],
        'addresses': addresses,


    }
    return HttpResponse(template.render(context,request))

def test4(request):
    template = loader.get_template('template4.html')
    context = {
        'name': '홍길동',
    }
    return HttpResponse(template.render(context,request))

def test5(request):
    template = loader.get_template('template5.html')
    addresses = Address.objects.all().values()
    context = {
        'addresses': addresses,
    }
    return HttpResponse(template.render(context,request))

def test6(request):
    template = loader.get_template('template6.html')
    addresses = Address.objects.all().values()
    context = {
        'addresses': addresses,
    }
    return HttpResponse(template.render(context,request))

def test7(request):
    template = loader.get_template('template7.html')
    addresses = Address.objects.all().values()
    context = {
        'addresses': addresses,
    }
    return HttpResponse(template.render(context,request))

def test8(request):
    template = loader.get_template('template8.html')
    addresses = Address.objects.all().values()
    context = {
        'addresses': addresses,
    }
    return HttpResponse(template.render(context,request))