from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    pass
    # list_display = ['id','name','source','contact_type','contact','consultant','consult_content','status','date']
    # list_filter = ['source','consultant','status','date']
    # search_fields = ['contact','consultant__name']

    # readonly_fields = ['status','contact']
    # filter_horizontal = ['consult_courses',]

    # actions = ['change_status',]
    # def change_status(self,request,querysets):
    #     querysets.update(status=1)

# class CourseRecordAdmin(admin.ModelAdmin):
    # list_display = ['class_grade','day_num','has_homework']
    #list_per_page = 2
    # list_editable = ['has_homework',]


# 注册
admin.site.register(User,UserAdmin)

