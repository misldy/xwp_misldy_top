from cProfile import label
import re

from django import forms
from django.contrib.auth import get_user_model
from .models import UserExtension

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(
        label="用户名", # 设置用户名提示标签
        max_length=150, # 设置表单最大长度，与models一致为150
        widget=forms.TextInput(attrs={
            'class': 'form-control',        # 设置表格样式
            'placeholder': '用户名',         # 设置提示信息
            'autofocus': 'autofocus'}),     # 设置首次打开页面自动聚焦
    )
    password = forms.CharField(
        label="密码",
        max_length=256,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '密码',
            'autocomplete': 'pwd'}),
    )
    remember = forms.BooleanField(
        required = None,
        initial="checked",
        widget=forms.CheckboxInput(attrs={
            'type': 'checkbox',},)
    )
    
    class Meta:
        model = User

class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        label="用户名",
        max_length=150,
        min_length=6,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '用户名',
            'autofocus': 'autofocus'}),
    )
    password1 = forms.CharField(
        label="密码",
        max_length=256,
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '密码，密码需包含：字母、数字、符号',}),
    )
    password2 = forms.CharField(
        label="确认密码",
        max_length=256,
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '确认密码，密码需包含：字母、数字、符号',}),
    )
    email = forms.EmailField(
        label="邮箱地址",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': '邮箱',}),
    )
    phone = forms.CharField(
        label= "手机号",
        max_length=20,
        widget = forms.TextInput(attrs={'class': 'form-control',}),
    )
    birthday = forms.DateField(
        label= "生日",
        widget = forms.widgets.DateInput(attrs={'class': 'form-control',}),
    )
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        user_exists = User.objects.filter(username=username).exists()
        if user_exists:
            raise forms.ValidationError("用户名已存在,请更新用户名")
        else:
            return username
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            raise forms.ValidationError("邮箱已存在,请更新邮箱")
        else:
            return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        level_weak = re.match(r'^((\d+)|([A-Za-z]+)|(\W+))$', password1)
        level_middle = re.match(r'([0-9]+(\W+|\_+|[A-Za-z]+))+|([A-Za-z]+(\W+|\_+|\d+))+|((\W+|\_+)+(\d+|\w+))+',password1)
        level_strong = re.match(r'(\w+|\W+)+',password1)
        if level_weak:
            password_level = 'weak'
        else:
            if (level_middle and len(level_middle.group())==len(password1)):
                password_level = 'middle'
            else:
                if level_strong and len(level_strong.group())==len(password1):
                    password_level = 'strong'
                else:
                    password_level = 'none'
        if password1 == password2:
            if password_level is 'strong':
                return password1
            elif password_level is 'middle':
                raise forms.ValidationError("密码较弱，请更换密码！密码需包含：字母、数字、符号")
            else:
                raise forms.ValidationError("密码为单一字符，请更换密码！密码需包含：字母、数字、符号")
        else:
            raise forms.ValidationError("密码输入不一致,请重试")

class UserExtensionFrom(forms.ModelForm):
    
    class Meta:
        model = UserExtension
        fields = ('birthday', 'phone')
        
        labels = {
            "birthday": "生日",
            "phone": "手机号"
        }
        
        widgets = {
            "birthday": forms.widgets.DateInput(attrs={'class': 'form-control',}),
            "phone": forms.widgets.TextInput(attrs={'class': 'form-control',})
        }