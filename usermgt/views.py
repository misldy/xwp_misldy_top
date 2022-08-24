from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.generic import FormView, CreateView, View, UpdateView
from django.shortcuts import redirect, render

User = get_user_model()

from usermgt.forms import LoginForm, RegisterForm
from usermgt.models import UserExtension

class LoginViwe(FormView):
    """ 用户登录视图 """
    template_name = 'usermgt/login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        else:
            login_form = self.form_class()
            return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        login_form = self.form_class(request.POST)
        message = "请检查填写的内容!"
        if login_form.is_valid():
            # .cleaned_data洗出合法数据
            data = login_form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                # 判断用户是否勾选记住登录
                if data['remember']:
                    request.session.set_expiry(60*60*24*30)
                else:
                    request.session.set_expiry(0)
                print(login_form)
                return redirect("/")
            else:
                message =  "账号或密码输入有误,请重新输入!"
        elif not login_form.errors:
            message = "账号密码输入有误。请检查填写的内容~"
        return render(request, self.template_name, locals())


class RegisterView(CreateView):
    template_name = 'usermgt/register.html'
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        else:
            register_form = self.form_class()
            return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        register_form = self.form_class(request.POST)
        if register_form.is_valid():  # 获取数据
            new_user = register_form.save(commit=False)
            # 设置密码
            new_user.set_password(register_form.cleaned_data['password1'])
            
            new_user.save()
            
            # 设置手机号
            new_user.extension.phone = register_form.cleaned_data['phone']
            # 设置生日
            new_user.extension.birthday = register_form.cleaned_data['birthday']
            # 保存好数据后立即登录并返回博客列表页面
            login(request, new_user)
            return redirect("/")
        elif not register_form.errors:
            message = "注册表单输入有误。请检查填写的内容~"
        return render(request, self.template_name, locals())


class LogoutView(View):
    """ 用户登出 """
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect("/")
        else:
            message = "您无权限操作此账号推出登录~"
        
    def post(self, request):
        return self.get(request)

class UserEditView(UpdateView):
    # model = UserExtension
    # fields = ['user_id', 'birthday', 'phone']
    template_name = 'usermgt/user_edit_form.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return UserExtension.objects.filter()
