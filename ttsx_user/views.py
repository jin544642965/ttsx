# coding:utf-8


from django.shortcuts import render, redirect
from models import *
from hashlib import sha1
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
import datetime

from ttsx_goods.models import GoodsInfo
# Create your views here.


# 登陆装饰器
def user_login(func):
    def func1(req, *args, **kwargs):
        if req.session.has_key('uid'):
            # 如果登陆成功继续执行视图
            return func(req, *args, **kwargs)
        else:
            return HttpResponseRedirect('/user/login/')
    return func1


def islogin(request):
    islogin = False
    if request.session.has_key('uid'):
        islogin = True
    return JsonResponse({'islogin': islogin})


def register(req):
    context = {'title': '注册'}
    return render(req, 'ttsx_user/register.html', context)


def register_handle(req):
    # 接收数据
    post = req.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    umail = post.get('email')
    # 加密
    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()

    # 创建模型对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd_sha1
    user.umail = umail
    user.save()

    # 完成后转向到登陆页
    return HttpResponseRedirect('/user/login/')


# 校验注册合法性
def register_valid(req):
    uname = req.GET.get('uname')
    result = UserInfo.objects.filter(uname=uname).count()

    # 构造字典数据
    context = {'valid': result}
    # 用json的方式返回数据给前端
    return JsonResponse(context)


# 显示登陆
def login(req):
    uname = req.COOKIES.get('uname', '')
    context = {'title': '登陆', 'uname': uname}
    return render(req, 'ttsx_user/login.html', context)


def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/user/login/')


# 处理登陆请求
def login_handle(req):
    post = req.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    uname_jz = post.get('name_jz', '0')
    print upwd
    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()

    context = {'title': '登陆', 'uname': uname, 'upwd': upwd}
    users = UserInfo.objects.filter(uname=uname)

    if len(users) == 0:
        # 用户名错误
        context['name_error'] = '1'
        return render(req, 'ttsx_user/login.html', context)
    else:
        if users[0].upwd == upwd_sha1:
            # 登陆成功,返回到用户中心
            # 记录登陆的用户
            req.session['uid'] = users[0].id
            req.session['uname'] = uname

            # 记住用户名，存入cookie就好,记录路径
            path = req.session.get('url_path', '/')
            response = HttpResponseRedirect(path)

            if uname_jz == "1":
                response.set_cookie('uname', uname, expires=datetime.datetime.now() + datetime.timedelta(days=7))
            else:
                response.set_cookie('uname', '', max_age=-1)
            return response

        else:
            # 密码错误
            context['pwd_error'] = '1'
            return render(req, 'ttsx_user/login.html', context)


@user_login
def info(req):
    user = UserInfo.objects.get(pk=req.session['uid'])

    gids = req.COOKIES.get('goods_ids', '').split(',')

    gids.pop()
    glist = []
    for gid in gids:
       glist.append(GoodsInfo.objects.get(id=gid))
    context = {'title': '用户中心', 'user': user, 'glist': glist}
    return render(req, 'ttsx_user/user_center_info.html', context)


@user_login
def order(req):
    context = {'title': '用户订单'}
    return render(req, 'ttsx_user/user_center_order.html', context)


@user_login
def site(req):
    user = UserInfo.objects.get(pk=req.session['uid'])
    if req.method == "POST":
        user.ushou = req.POST.get("ushou")
        user.uaddress = req.POST.get("uaddress")
        user.ucode = req.POST.get("ucode")
        user.uphone = req.POST.get("uphone")
        user.save
    context = {'title': '收货地址', 'user': user}
    return render(req, 'ttsx_user/user_center_site.html', context)

