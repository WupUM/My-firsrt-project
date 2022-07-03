# login/views.py

from django.shortcuts import render, redirect
from . import models
from .forms import UserForm, RegisterForm
import hashlib
from django import forms
from login import models
from django.forms import ModelForm


def index(request):
    user_list = models.User.objects.all()
    print(user_list)
    context = {"user_list": user_list}
    return render(request, 'login/index.html', context)


def login(request):
    if request.session.get('is_login', None):
        return redirect("/")
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)

                if user.password == hash_code(password):  # 哈希值和数据库内的值进行比对
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户
                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = hash_code(password1)  # 使用加密密码
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/')
    request.session.flush()

    return redirect('/')


def hash_code(s, salt='site_login'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


def detail(request, id):
    user = models.User.objects.get(id=id)
    return render(request, "login/detail.html", context={"user": user})


class TestForm(forms.ModelForm):
    class Meta:
        model = models.Test1
        fields = ["Q1", "Q2", "Q3"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加了class="form-control"
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def test(request, nid):
    if nid != request.session['user_id']:
        print('Invalid request')
        return redirect('/')

    row_object = models.Test1.objects.filter(user_id=nid).first()
    if request.method == "GET":
        form = TestForm(instance=row_object)
        return render(request, 'test.html', {"form": form})

    if not row_object:
        row_object = models.Test1.objects.create(user_id=nid)

    form = TestForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()

        return redirect('/')

    return render(request, 'test.html', {"form": form})


def create(request):
    test_inst, created = models.Test1.objects.update_or_create(user_id=request.session['user_id'])
    form = TestForm(instance=test_inst)
    return render(request, 'test.html', {"form": form})
    # models.Test1.objects.create(
    #     user_id=request.session['user_id'],
    # )
