from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.template import loader
from .models import *
from django.utils import timezone
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    template = loader.get_template('index.html')
    login_session = request.session
    if login_session.get("member") is None:
        login_state = 0
    else:
        login_state = 1
    context = {
        'login_state': login_state,
        'login_session': login_session.get("member"),
    }
    return HttpResponse(template.render(context, request))


# https://docs.djangoproject.com/en/4.0/ref/models/querysets/  # 쿼리문API
def list(request):
    # addresses = Address.objects.all().values()
    
    # [=] where name = str
    # addresses = Address.objects.filter(name="홍길동").values()
    # [and] where name = str and addr = str2
    # addresses = Address.objects.filter(name="홍길동", addr="서울").values()
    # [or 1] where name = str, addr = addr1 or name = str, addr=addr2
    # addresses = Address.objects.filter(name="홍길동", addr="서울").values() \
    #             | Address.objects.filter(name="홍길동", addr="한양").values()
    # [or 2] where name = str, addr = addr1 or name = str, addr=addr2
    # addresses = Address.objects.filter(Q(name="홍길동", addr="한양") \
    #             | Q(addr="서울")).values()
    # [like 1] where name like %str
    # addresses = Address.objects.filter(name__startswith="이").values()
    # [like 2] where name like str%
    # addresses = Address.objects.filter(name__endswith="동").values()
    # [like 3] where name like %str%
    # addresses = Address.objects.filter(name__contains="홍").values()
    # [in] where name in (a, b, c)
    # addresses = Address.objects.filter(name__in=["김유신", "이순신"]).values()
    # [greater] where rdate > 날짜, 시간
    # addresses = Address.objects.filter(rdate__gt="2022-07-28 10:04:06").values()

    # [order by]
    # addresses = Address.objects.all().values().order_by("name").order_by("rdate")
    addresses = Address.objects.all().values().order_by("-name", "addr")
    context = {
        'addresses': addresses,
    }
    template = loader.get_template('list.html')
    return HttpResponse(template.render(context, request))


def write(request):
    template = loader.get_template('write.html')
    return HttpResponse(template.render(request=request))


def write_ok(request):
    x = request.POST["name"]
    y = request.POST["addr"]
    address = Address(name=x, addr=y)
    address.save()
    return HttpResponseRedirect(reverse('list'))


def delete(request, id):
    addr = Address.objects.get(id=id)
    addr.delete()
    return HttpResponseRedirect(reverse('list'))


def update(request, id):
    template = loader.get_template('update.html')
    address = Address.objects.get(id=id)
    context = {
        'address': address,
    }
    return HttpResponse(template.render(context, request))


def update_ok(request, id):
    x = request.POST["name"]
    y = request.POST["addr"]
    now = timezone.now()
    address = Address.objects.get(id=id)
    address.name = x
    address.addr = y
    address.rdate = now
    address.save()
    return HttpResponseRedirect(reverse('list'))


# 게시판
def b_list(request):
    member_session = request.session
    if member_session.get("member") is not None:
        print(member_session["member"])
    else:
        pass
    ps = request.GET.get("ps")
    p_num = request.session

    if ps is None:
        pass
    else:
        p_num["page"] = ps
    if p_num.get("page") is None:
        nums = 5
    else:
        nums = int(p_num["page"])
    selects = [0, 3, 5, 10]
    template = loader.get_template('board/list.html')
    board_list = Board.objects.all().values().order_by('id')
    paginator = Paginator(board_list, nums)
    total_page = paginator.num_pages
    pages = paginator.page_range
    page = request.GET.get('page')

    boards = paginator.get_page(page)
    context = {
        'boards': boards,
        'total_page': total_page,
        'pages': pages,
        'ps': selects.index(nums),
        'b_count': len(board_list),
    }

    response = HttpResponse(template.render(context, request))
    return response


def b_write(request):
    member_session = request.session
    member_info = ""
    if member_session.get("member") is not None:
        # print(member_session["member"])
        member_info = member_session["member"]
    else:
        pass

    context = {
        'member_info': member_info,
    }
    template = loader.get_template('board/write.html')
    return HttpResponse(template.render(context, request))


def b_write_ok(request):
    writer = request.POST["writer"]
    email = request.POST["email"]
    subject = request.POST["subject"]
    content = request.POST["content"]
    board = Board(writer=writer, email=email, subject=subject, content=content)
    board.save()
    return HttpResponseRedirect(reverse('b_list'))


def b_content(request, id):
    board = Board.objects.get(id=id)
    context = {
        'board': board,
    }
    template = loader.get_template('board/content.html')
    return HttpResponse(template.render(context, request))


def b_update(request, id):
    board = Board.objects.get(id=id)
    context = {
        'board': board,
    }
    template = loader.get_template('board/update.html')
    return HttpResponse(template.render(context, request))


def b_update_ok(request, id):
    board = Board.objects.get(id=id)
    board.writer = request.POST["writer"]
    board.email = request.POST["email"]
    board.subject = request.POST["subject"]
    board.content = request.POST["content"]
    board.save()
    return HttpResponseRedirect(reverse('b_list'))


def b_delete(request, id):
    board = Board.objects.get(id=id)
    board.delete()
    return HttpResponseRedirect(reverse('b_list'))


def login(request):
    members = Member.objects.all().values().order_by('id')
    # 초기 데이터 세팅
    mlist = [['홍길동', 'hong@hanmail.net', '1234', '0101231234']
        ,['이순신', 'lee@hanmail.net', '1234', '0101231235']
        ,['강감찬', 'gang@hanmail.net', '1234', '0101231236']
        ,['한예슬', 'han@hanmail.net', '1234', '0101231237']
        ,['장동건', 'jang@hanmail.net', '1234', '0101231238']
        ,['손님', 'guest@hanmail.net', '1234', '0101231239']]

    for x in range(0, len(mlist)):
        try:
            members.get(email=mlist[x][1])
        except ObjectDoesNotExist:
            m1 = Member()
            m1.name = mlist[x][0]
            m1.email = mlist[x][1]
            m1.pwd = mlist[x][2]
            m1.phone = mlist[x][3]
            m1.save()
            pass

    # 로그인 세션 체크
    member_session = request.session
    if member_session.get("member") is not None:
        print(member_session["member"])
        return redirect('index')
    else:
        pass
    # 로그인 체크
    # login_state = "0"
    # login_msg = "msg"
    login_msg = {"state": "0", "msg": "메시지"}
    if request.method == "POST":
        try:
            member = members.get(email=request.POST["email"])
            if member["pwd"] == request.POST["pwd"]:
                id = member['id']
                name = member['name']
                email = member['email']
                phone = member['phone']
                rdate = member['rdate'].strftime('%Y-%m-%d %H시 %m분')
                udate = member['udate'].strftime('%Y-%m-%d %H시 %m분')
                member_session["member"] = {'id': str(id), 'name': name, 'email': email, 'phone': phone,
                                            'rdate': rdate, 'udate': udate}
                print("로그인 성공")
                login_msg["state"] = "1"
                login_msg["msg"] = "로그인 성공"
                return HttpResponseRedirect(reverse('index'))
            else:
                print("비밀번호 틀림")
                login_msg["state"] = "2"
                login_msg["msg"] = "아이디 또는 비밀번호가 일치 하지 않습니다."
        except ObjectDoesNotExist:
            print("로그인 실패")
            login_msg["state"] = "-1"
            login_msg["msg"] = "아이디가 존재하지 않습니다."
            print(request.POST["email"], request.POST["pwd"])
    else:
        pass
    context = {
        'login_msg': login_msg,
    }
    template = loader.get_template('login.html')
    return HttpResponse(template.render(context, request))


def logout(request):
    member_session = request.session
    if member_session.get("member") is not None:
        del member_session["member"]
    else:
        pass
    return redirect('index')
