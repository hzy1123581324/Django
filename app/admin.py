from django.contrib import admin
from .models.models import User,Role,Recommend,UserDetails
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('名称', {'fields': ['nickname','username']}),
        # ('密码', {'fields': ['password','paypassword']}),
    ]
    # fields = ['loginTime']
    # list_display = ['id','name','source','contact_type','contact','consultant','consult_content','status','date']
    # list_filter = ['source','consultant','status','date']
    search_fields = ['username','nickname']

    model = UserDetails
    # class Meta:
    #     # fields = ('email', 'name')
    #     fields = "__all__"

    # def clean_password2(self):
    #     # Check that the two password entries match
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords don't match")
    #     return password2

    # readonly_fields = ['status','contact']
    # filter_horizontal = ['consult_courses',]

    # actions = ['change_status',]
    # def change_status(self,request,querysets):
    #     querysets.update(status=1)

# class CourseRecordAdmin(admin.ModelAdmin):
    # list_display = ['class_grade','day_num','has_homework']
    #list_per_page = 2
    # list_editable = ['has_homework',]

class RoleAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ('名称', {'fields': ['nickname','username']}),
    #     ('密码', {'fields': ['password','paypassword']}),
    # ]
    # fields = ['name', 'user',]
    pass

class RecommendAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ('名称', {'fields': ['nickname','username']}),
    #     ('密码', {'fields': ['password','paypassword']}),
    # ]
    fields = ['parent', 'child',]

# 注册
admin.site.register(User,UserAdmin)
admin.site.register(Role,RoleAdmin)
admin.site.register(Recommend,RecommendAdmin)


