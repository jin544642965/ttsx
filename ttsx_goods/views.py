# coding:utf-8

from django.shortcuts import render
from models import *
from django.core.paginator import Paginator
from haystack.generic_views import SearchView

# Create your views here.


def index(request):
    goods_list = []
    # 查询分类对象

    # 查询每个分类中最新的4个商品

    # 查询每个分类中最火的4个商品
    type_list = TypeInfo.objects.all()

    for kinds in type_list:
        # kinds.goodsinfo分类对应的所有商品
        nlist = kinds.goodsinfo_set.order_by('-id')[0:4]
        clist =kinds.goodsinfo_set.order_by('-gclick')[0:4]
        goods_list.append({'kinds': kinds, 'nlist': nlist, 'clist': clist})
    context = {"title": "首页", 'glist': goods_list, 'cart_show': '1'}
    return render(request, 'ttsx_goods/index.html', context)


def goods_list(request, tid, pindex):
    # 商品总共有6个分类,查询出分类对象
    kinds = TypeInfo.objects.get(pk=int(tid))
    new_list = kinds.goodsinfo_set.order_by('-id')[0:2]

    # 指定排序规则
    orderby_str = '-id'
    sort = request.GET.get('sort')
    sort_price = request.GET.get('sort_price', 'sort_price_asc')

    if sort == 'default':
        orderby_str = '-id'
    if sort == 'price':
        # 指定价格升序还是降序
        if sort_price == 'sort_price_asc':
            orderby_str = 'gprice'
            # sort_price = 'sort_price_desc'
        elif sort_price == 'sort_price_desc':
            orderby_str = '-gprice'
            # sort_price = 'sort_price_asc'
    if sort == 'gclick':
        orderby_str = '-gclick'

    # 查询：当前分类的所有商品，按每页15个来显示
    glist = kinds.goodsinfo_set.order_by(orderby_str)
    # 创建一个分页类对象
    paginator = Paginator(glist, 5)
    pindex1 = int(pindex)

    if pindex1 < 1:
        pindex1 = 1
    elif pindex1 > paginator.num_pages:
        pindex1 = paginator.num_pages
    page = paginator.page(pindex1)
    context = {'title': '商品列表页', 'cart_show': '1', 'kinds': kinds, 'new_list': new_list, 'page': page, 'sort': sort, 'sort_price': sort_price}
    return render(request, 'ttsx_goods/goods_list.html', context)


def detail(request, id):
    try:
        goods = GoodsInfo.objects.get(pk=int(id))
        goods.gclick += 1
        goods.save()
        new_list = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
        context = {'title': '商品详细页', 'cart_show': '1', 'goods': goods, 'new_list': new_list}
        response = render(request, 'ttsx_goods/detail.html', context)
        # 保存最近浏览[1,2,3,4,5]
        gids = request.COOKIES.get('goods_ids', '').split(',')
        # 判断这个编号是否存在，如果存在则删除，然后加到最前面
        if id in gids:
            gids.remove(id)
        gids.insert(0, id)
        if len(gids) > 5:
            # 将空格弹出
            gids.pop()
        response.set_cookie('goods_ids', ','.join(gids), max_age=60*60*24*7)
        return response
    except:
        return render(request, '404.html')


class MySearchView(SearchView):

    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        context['cart_show'] = 1  # 传递上下文原有模板文件，显示购物车
        page_range = []
        page = context.get('page_obj')   # 获取当前页面对象
        if page.paginator.num_pages < 5:
            page_range = page.paginator.page_range
        elif page.number <= 2:
            page_range = range(1, 6)
        elif page.number >= page.paginator.num_pages-1:
            page_range = range(page.paginator.num_pages-4, page.paginator.num_pages+1)
        else:
            page_range = range(page.number-2, page.number+3)
        context['page_range'] = page_range
        print context
        return context

