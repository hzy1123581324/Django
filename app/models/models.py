from django.db import models

# Create your models here.

class Banner(models.Model):
    """
    轮播图表
    img:图片链接
    url: 跳转链接
    show: 是否显示
    weight:权重（排列）
    classify: 分类
    """
    # img = models.CharField(max_length=64,unique=True)
    # menus = models.ManyToManyField("Menus",blank=True)
    
class User(models.Model):
    """
    用户表
    id: 用户id 自增
 
    """
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    # 用户id 自增
    nickname = models.CharField(max_length=64,unique=True)
    # 昵称
    username = models.CharField(max_length=32)
    # 真实姓名
    password = models.CharField(max_length=64)
    # 登录密码
    paypassword = models.CharField(max_length=6)
    # 支付密码
    create = models.DateField(auto_now_add=True)
    # 用户创建时间
    # loginTime = models.DateField(auto_now_add=True)
    # 用户登录时间
    
    # menus = models.ManyToManyField("Menus",blank=True)
    class Meta:
        verbose_name_plural  = '用户表'

    def __str__(self):
        return "%s" %(self.username,)


class Role(models.Model):
    """
    身份

    权限表
    id: 权限id
    name: 权限名称//
    user: 权限表多对多对应的用户表
    """
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=32,)
    user = models.ManyToManyField(User)

class BrowseRecord(models.Model):
    """
    浏览记录

    start: 开始浏览时间
    end: 结束时间
    browseId:浏览对象id
    user: 浏览记录表一对一对应用户表
    """
    start = models.DateField()
    end = models.DateField(auto_now_add=True,verbose_name='结束时间')
    browseId = models.SmallIntegerField(choices=[(0, '脱产'), (1, '周末'), (2, '网络班')], default=0)
    # user = models.OneToOneField('User')
    def __str__(self):
        # 在admin中展示 
        return "%s" % self.start

class wallet(models.Model):
    '''
    根据权限显示对应数据
    钱包表
    
    '''
    

class AdvertiserInformation(models.Model):
    '''
    广告商信息

    type: 展示广告的类型
    投放区域

    '''
    pass

class relation(models.Model):
    """
    用户与用户之间的关系表

    """
    pass


class Recommend(models.Model):
    '''
    推荐表
    '''
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    

