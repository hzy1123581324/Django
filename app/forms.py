from django import forms 
from django.forms import fields


class UserForm(forms.Form):
    username = fields.CharField()


class UploadFileForm(forms.Form):
    '''
    表单商城
    '''
    title = forms.CharField(max_length=50)
    file = forms.FileField()