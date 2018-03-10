项目设计：
这是一个垂直电商，只针对生鲜水果的一个电商平台
实现的功能：
首页：商品的分类展示
列表页：某一种类商品的商品显示
商品详情页：单个商品的详细信息，名称，价格等
购物车页：想要购买的香品列表，总的价格信息
用户登录注册页：账号密码登陆，注册信息
用户中心页面：用户的账号信息，浏览记录
订单页：已经支付的商品和未支付的商品列表显示
---------------------------------------------
模型类设计（数据库设计）：
商品分类TypeInfo
title    商品分类标题
isDelete  是否删除分类

商品GoodsInfo
gtitle
gprice
gunit
gkucun
gdesc
gtype
gpic
gclick
gsubtitle
isDelete

购物车CartInfo
#谁买了多少个
user （哪个用户买的商品）
goods （购物车中有哪些商品，作为外键，对应商品表）
count（商品的数量，买了多少件商品）

用户UserInfo
uname
upwd
uemail
uaddress
ucode
uphone
isDelete

订单orderInfo
order_id (作为主键)
totlal 订单的总数
user （订单关联到哪个用户，外键外链到UserInfo）
state  订单的支付状态（已支付/未支付）

订单详细
order (外键关联到订单表Orderinfo)
goods（外键关联到商品表GoodsInfo）
price（订单的实际价格）
count（订单的数量）

-------------------------------------
功能方法实现
商品模块的功能
   1.商品首页： 定义函数def index，for遍历出数据库中的商品 return
   2.商品列表：，def goods_list
查看某个商品属于哪个分类,在商品分类表TypeInfo查询出分类对象，  
 商品列表排序商品
 商品列表分页
   3.商品详细：
记录商品点击数到数据库gclick
记录用户浏览的商品gids
用户最近浏览的5个商品

   4.搜索显示商品页MysearchView
分页显示商品功能


购物车功能实现
1.添加到购物车def add
在数据库查询用户购物车中的商品， 并显示在前端
2.统计购物车中商品数量def count
3.购物车的展示页def index
4.修改购物车中商品数量def edit
5.购物车中商品删除
6.购物车中去提交订单

订单功能实现：
1.处理订单do_order
用到事物sid，如果有个订单不足，则放弃执行修改
首先创建一个保存点transcation
根据时间函数datetime创建订单编号
判断购物车的中的数量与商品库存数量，如果正常则修改数据库，否则回滚到原来的事物点sid（transaction.savepoint_rollback）

