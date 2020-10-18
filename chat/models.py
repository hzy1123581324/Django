from django.db import models
from utils.baseModel import BaseModel

# Create your models here.


class User(BaseModel):
    """
    用户表
    id: 继承BaseModel

    """
    nickname = models.CharField(max_length=64, unique=True, verbose_name='昵称')
    # 昵称
    loginPassword = models.CharField(max_length=64)
    # 登录密码
    avatar = models.ImageField(
        upload_to='img/%Y/%m/%d', verbose_name='用户头像')
    # 用户登录时间

    # menus = models.ManyToManyField("Menus",blank=True)

    class Meta:
        verbose_name_plural = '用户表'

    def __str__(self):
        return "%s" % (self.nickname,)


class UserDetails(BaseModel):
    '''
    用户详情
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # time = models.OneToOneField('UserTime', on_delete=models.CASCADE)
    # role = models.ForeignKey('Role', on_delete=models.CASCADE)
    realname = models.CharField(max_length=32, verbose_name='真实姓名')
    # 真实姓名
    paypassword = models.CharField(max_length=6, null=True)
    # 支付密码
    sex_choices = ((0, '保密'), (1, '男'), (2, '女'),)
    gender = models.PositiveSmallIntegerField(
        choices=sex_choices, blank=True, null=True, default=0)
    # 性别

    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    # 用户地址信息


class Address(BaseModel):
    '''
    用户地址信息
    '''
    pass


class Wallet(BaseModel):
    '''
    钱包
    '''
    pass


class Card(BaseModel):
    '''
    用户获取的卡片
    '''
    pass


class Empiric(BaseModel):
    '''
    用户的经验值
    '''
    pass


class Grade(BaseModel):
    '''
    用户的等级
    '''
    pass
