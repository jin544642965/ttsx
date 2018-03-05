# coding:utf-8
from django.shortcuts import render
from django.http import JsonResponse
from models import *
from django.db.models import Sum
from ttsx_user.views import user_login
from ttsx_user.models import UserInfo
# Create your views here.


def add(request):
    try:
        uid = request.session.get('uid')
        gid = request.GET.get('gid')
        count = int(request.GET.get('count', '1'))

        carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)

        if len(carts) == 1:
            cart = carts[0]
            cart.count += count
            cart.save()
        else:
            cart = CartInfo()
            cart.user_id = uid
            cart.goods_id = gid
            cart.count = count
            cart.save()
        return JsonResponse({'isadd': True})
    except:
        return JsonResponse({'isadd': False})


def count(request):
    uid = request.session.get('uid')
    cart_count = CartInfo.objects.aggregate(Sum('count')).get('count__sum')  # 求表中字段的和
    if cart_count is None:
        cart_count = 0
    return JsonResponse({'cart_count': cart_count})


@user_login
def index(request):
    uid = request.session.get('uid')
    cart_list = CartInfo.objects.filter(user_id=uid)

    context = {'title': "购物车", 'cart_list': cart_list}
    return render(request, 'ttsx_cart/cart.html', context)


def edit(request):
    id = int(request.GET.get('id'))
    count = int(request.GET.get('count'))
    cart = CartInfo.objects.get(pk=id)
    cart.count = count
    cart.save()
    return JsonResponse({'ok': True})


def delete(request):
    id = int(request.GET.get('id'))
    cart = CartInfo.objects.get(pk=id)
    cart.delete()
    return JsonResponse({'ok': True})


def order(request):
    user = UserInfo.objects.get(pk=request.session.get('uid'))
    cart_ids = request.POST.getlist('cart_id')  # 多个ID值 ,列表形式
    cart_list = CartInfo.objects.filter(id__in=cart_ids)  # 循环遍历
    c_ids = ','.join(cart_ids)  # 构成字符串类型用逗号分隔
    context = {'title': "提交订单", 'user': user, 'cart_list': cart_list, 'c_ids': c_ids}
    return render(request, 'ttsx_cart/order.html', context)
