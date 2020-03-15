from django.db import models

# Create your models here.

class User(models.Model):
    """
    用户表
    id: 用户id 自增
 
    """
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    # verbose_name
    # 用户id 自增
    nickname = models.CharField(max_length=64,unique=True)
    # 昵称
    username = models.CharField(max_length=32)
    # 真实姓名
    password = models.CharField(max_length=64)
    # 登录密码

    # 用户登录时间
    
    # menus = models.ManyToManyField("Menus",blank=True)

    class Meta:
        verbose_name_plural  = '用户表'

    def __str__(self):
        return "%s" %(self.username,)
class UserDetails(models.Model):
    '''
    用户详情
    '''
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    time = models.OneToOneField('UserTime',on_delete = models.CASCADE)
    role = models.ForeignKey('Role',on_delete = models.CASCADE)
    paypassword = models.CharField(max_length=6)
    # 支付密码
    sex_choices = ((0,'保密')，(1,'男'),(2,'女'),)
    gender = models.PositiveSmallIntegerField(choices=sex_choices,blank=True,null=True,default=0)
    # 性别

class UserTime(models.Model):
    '''
    用户行为时间表
    loginTime 登录时间
    create 创建时间
    '''
    # auto_now   自动创建---无论添加或修改，都是当前操作的时间
    # auto_now_add 自动创建---永远是创建时的时间
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    create = models.DateField(auto_now_add=True)
    loginTime = models.DateField(auto_now=True)
    

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
    parent = models.ForeignKey(User,on_delete=models.SET_NULL)
    child = models.ForeignKey(User,on_delete)
   
    

