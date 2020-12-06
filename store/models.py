from django.db import models
from chat.models import User, Address
from utils.baseModel import BaseModel, CategoryModel
# Create your models here.
# 多商家数据库


# class BaseModel(models.Model):
#     """为模型类补充字段"""

#     create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
#     update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

#     class Meta:
#         # abstract: 抽象
#         abstract = True  # 说明是抽象模型类, 用于继承使用，数据库迁移时不会创建BaseModel的表


class Stores(BaseModel):
    """
    店铺名称（默认是平台）
    店铺 id 自动生成继承BaseModel

    店铺地址
    店铺经纬度
    联系方式（选择 电话，微信，qq）
    店铺所有者
    店铺营业证书
    店铺介绍
    收款账户
    店员
    """
    CONTACTTYPE = (
        (1, "电话"),
        (2, "微信"),
        (3, "QQ"),
    )
    lon = models.DecimalField(
        max_digits=8, decimal_places=3, verbose_name='经度')
    lat = models.DecimalField(
        max_digits=8, decimal_places=3, verbose_name='纬度')
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    contacttype = models.IntegerField(
        choices=CONTACTTYPE, default='1', verbose_name='联系类型')
    contact = models.CharField(blank=True, max_length=300, verbose_name='联系内容')
    content = models.TextField(default="", verbose_name="店铺详情")
    clerk = models.ForeignKey(
        'Clerk', on_delete=models.CASCADE, verbose_name='店员')


class Clerk(BaseModel):
    '''
        店员表

    '''
    name = models.CharField(max_length=100, default='', verbose_name='职位')
    user = models.ManyToManyField(User, '店员')


class Commodity(BaseModel):
    '''
    商品表

    商品 id 自动生成继承BaseModel
    商品短标题
    商品长标题
    商品价格
    商品限时价格
    商品缩略图
    商品主图
    商品标签    （跟标签表是多对多关系）
    商品优惠券 （跟优惠券表是多对多关系）


    '''
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='', verbose_name='名称')
    caption = models.CharField(max_length=100, verbose_name='副标题')
    sales = models.IntegerField(default=0, verbose_name='销量')
    stock = models.IntegerField(default=0, verbose_name='库存')
    sales = models.IntegerField(default=0, verbose_name='销量')
    comments = models.IntegerField(default=0, verbose_name='评价数')
    is_launched = models.BooleanField(default=True, verbose_name='是否上架销售')
    main_image_url = models.CharField(max_length=200, default='',
                                      null=True, verbose_name='主图片')
    thumbnail = models.CharField(max_length=200, default='',
                                 null=True, blank=True, verbose_name='缩略图')
    coupons = models.ForeignKey(
        'Coupons', default='', blank=True, verbose_name='优惠券', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_sku'
        verbose_name = '商品SKU'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' % (self.id, self.name)


# class Category(BaseModel):
#     '''
#     商品类别
#     '''
#     name = models.CharField(max_length=30, verbose_name='分类名称')

#     class Meta:
#         verbose_name_plural = '商品分类'

#     def __str__(self):
#         return self.name


class GoodsCategory(BaseModel, CategoryModel):
    """
    商品类别
    """

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Brand(BaseModel):
    """
    品牌
    """
    name = models.CharField(max_length=20, default='', verbose_name='名称')
    logo = models.ImageField(verbose_name='Logo图片')
    first_letter = models.CharField(max_length=1, verbose_name='品牌首字母')

    class Meta:
        db_table = 'tb_brand'
        verbose_name = '品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CommodityDetails(BaseModel):
    '''
    商品详情表
    跟商品表是一对一关系
    字段：
    商品轮播图
    商品介绍  （富文本）
    是否收藏
    商品规格
    是否是实物（分为虚拟商品和实物商品，虚拟商品购买是没有收货地址，不可退款等）

    '''
    commodity = models.OneToOneField(Commodity, on_delete=models.CASCADE)


class Coupons(BaseModel):
    '''
    优惠券表

    '''
    # worth = models.
    pass


class Order(BaseModel):
    """
    商品订单
    订单id,
    商品id,
    数量，
    规格
    收货地址，
    优惠券（使用的优惠券）,
    留言：长文本
    用户


    """

    ORDER_STATUS_CHOICES = (
        (1, "待支付"),
        (2, "待发货"),
        (3, "待收货"),
        (4, "待评价"),
        (5, "已完成"),
        (6, "已取消"),
    )
    status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES,
                                      default=1, verbose_name="订单状态")

    class Meta:
        db_table = 'tb_order'
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class OrderDetails(BaseModel):

    '''
    订单详情
    '''

    # OrderDetails.PAY_METHODS_ENUM.get('CASH')   -->  1
    # OrderDetails.PAY_METHODS_ENUM.get('ALIPAY')   -->  2
    PAY_METHODS_ENUM = {
        "CASH": 1,          # 货到付款
        "ALIPAY": 2,        # 阿里支付
        "WXPAY": 3,         # 微信支付
        "BALANCE": 4        # 钱包余额支付

    }

    PAY_METHOD_CHOICES = (
        (1, "货到付款"),
        (2, "支付宝"),
        (3, "微信"),
        (4, "余额"),
        (5, '支付宝+余额'),
        (6, '微信+余额'),
    )
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    # 主键, 不会生成默认的主键id
    # order_id = models.CharField(
    #     max_length=64, verbose_name="订单号")
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="下单用户")
    address = models.ForeignKey(
        Address, on_delete=models.PROTECT, verbose_name="收获地址")
    total_count = models.IntegerField(default=1, verbose_name="商品总数")
    total_amount = models.DecimalField(max_digits=10,
                                       decimal_places=2, verbose_name="商品总金额")

    freight = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="运费")
    pay_method = models.SmallIntegerField(choices=PAY_METHOD_CHOICES,
                                          default=4, verbose_name="支付方式")

    actual_payment = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="实际付款")

    class Meta:
        db_table = "tb_order_info"
        verbose_name = '订单基本信息'
        verbose_name_plural = verbose_name


class OrderGoods(BaseModel):
    """
    订单商品
    """
    SCORE_CHOICES = (
        (0, '0分'),
        (1, '20分'),
        (2, '40分'),
        (3, '60分'),
        (4, '80分'),
        (5, '100分'),
    )

    order = models.ForeignKey(OrderDetails,
                              related_name='skus', on_delete=models.CASCADE, verbose_name="订单")
    # sku = models.ForeignKey(SKU, on_delete=models.PROTECT, verbose_name="订单商品")
    count = models.IntegerField(default=1, verbose_name="数量")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="单价")
    comment = models.TextField(default="", verbose_name="评价信息")
    score = models.SmallIntegerField(choices=SCORE_CHOICES,
                                     default=5, verbose_name='满意度评分')
    is_anonymous = models.BooleanField(default=False, verbose_name='是否匿名评价')
    is_commented = models.BooleanField(default=False, verbose_name='是否评价了')

    class Meta:
        db_table = "tb_order_goods"
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name
