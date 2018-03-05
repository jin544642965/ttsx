# coding:utf-8
from django.shortcuts import render, redirect
from django.db import  transaction
from models import *
from datetime import datetime
from ttsx_cart.models import CartInfo
# Create your views here.
"""
1.创建订单主表
2.接收所有的购物车请求
3.查询所有的购物车信息
4.逐个判断库存
5.库存足够
 创建详单，改写库存，计算总金额，删除购物车数据，
6.库存不够，则放弃之前的保存，转到购物车
"""


@transaction.atomic
def do_order(request):
    # 引入事物操作，如果有个订单中的库存不足，则放弃执行修改
    isok = True
    sid = transaction.savepoint()           #保存点，放到临时表
    try:
        # 1
        uid = request.session.get('uid')
        now_str = datetime.now().strftime('%Y%m%d%H%M%S')
        main = OrderMain()
        main.order_id = '%s%d' % (now_str, uid)
        main.user_id = uid
        main.save()

        # 2
        cart_ids = request.POST.get('cart_ids').split(',')  # '4,5,6' 只能接收字符串

        # 3
        cart_list = CartInfo.objects.filter(id__in=cart_ids)  # 列表
        total = 0
        for cart in cart_list:
            if cart.count <= cart.goods.gkucun:   # 5
                # 5.1
                detail = OrderDetail()
                detail.order = main
                detail.goods = cart.goods
                detail.count = cart.count
                detail.price = cart.goods.gprice
                detail.save()

                # 5.2
                cart.goods.gkucun -= cart.count
                cart.goods.save()

                # 5.3
                total += cart.count * cart.goods.gprice
                main.total = total
                main.save()


                # 5.4
                cart.delete()
            else:
                # 6 库存不够, 回滚
                isok = False
                transaction.savepoint_rollback(sid)
                break  # 如果失败，跳出循环
        if isok:  # for 循环正常
            transaction.savepoint_commit(sid)



    except:
        transaction.savepoint_rollback(sid)
        isok = False
    if isok:  # 正常就转到订单页面
        return redirect('/user/order/')
    else:
        return redirect('/cart/')
