from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, update_session_auth_hash, logout
from django.urls import reverse
from django.views import View

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from .serializers import AccountTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .forms import LoginForm

from .serializers import (
    UserRegSerializer
)

User = get_user_model()


class AccountLoginTokenObtainPairView(TokenObtainPairView):
    """用户登录接口"""
    serializer_class = AccountTokenObtainPairSerializer


class UserViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """
    用户注册
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        ret_dict = serializer.data
        # 签发token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        ret_dict["token"] = access_token
        ret_dict.pop('access')
        headers = self.get_success_headers(serializer.data)
        return Response(ret_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    @action(['post'], detail=False, url_name='password_change')
    def password_change(self, request, *args, **kwargs):

        data_p = request.data
        password_old = data_p.get('password', '')
        password_new = data_p.get('password2', '')
        data_p.pop('password2')

        # 检查用户名和密码是否正确
        user = request.user
        if user.check_password(password_old):
            user.set_password(password_new)
            user.save()
            update_session_auth_hash(request, user)
            # 重新签发token
            ret_dict = {}
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            ret_dict['code'] = 200
            ret_dict['msg'] = '密码修改成功'
            ret_dict["token"] = access_token
            headers = self.get_success_headers(ret_dict)
            return Response(ret_dict, status=status.HTTP_201_CREATED, headers=headers)
        else:
            data = {'code': 400, 'msg': '旧密码不对,修改失败!'}
            return Response(data)

    @action(['get'], detail=False, url_path='logout')
    def logout(self, request, *args, **kwargs):
        """实现退出登录逻辑"""
        print(request.user)
        data = {}
        if request.user.is_authenticated:
            # 清理session
            logout(request)
            data['code'] = 200
            data['msg'] = '退出登录成功'
        else:
            data['code'] = 400
            data['msg'] = '未登录,无需退出登录'
        # 退出登录，重定向到登录页
        # response = redirect(reverse('account:index'))
        # 退出登录时清除cookie中的username
        # response.delete_cookie('username')
        return Response(data=data)

    @action(['post'], detail=False, url_path='login')
    def login(self, request, *args, **kwargs):
        """
        用户登录
        """
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        # 登录
        user_obj = auth.authenticate(request, username=username, password=password)

        if user_obj is not None and user_obj.is_active:
            login(request, user_obj)
        return render(request, 'account/index.html', context={'user': user_obj})


def index(request):
    user_obj = request.user

    # 判断用户是否登录
    if not user_obj.is_authenticated:
        return redirect(reverse("account:login"))
    return render(request, 'account/index.html', context={'user': user_obj})


def password_change(request):
    """
       @api {post} api/modify_password/  3. 修改密码
       @apiDescription 修改密码
       @apiGroup 账号功能
       @apiParam {string} old_password 旧密码
       @apiParam {string} new_password 新密码
       @apiSuccessExample Success-Response:
           {
               'code': 0,
               'message': '修改密码成功'
           }
       @apiErrorExample Error-Response:
           {
               'code': 1,
               'message': '用户名不存在/修改密码失败'
           }
       """
    data = {'code': 200, 'msg': '密码修改成功!'}
    return Response(data)


class LoginView(View):
    """
    登录页面处理逻辑
    """
    template_name = "account/login.html"

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        # 判断用户是否登录
        if request.user.is_authenticated:
            next_url = request.GET.get("next", reverse("account:index"))
            return redirect(next_url)
        else:
            msg = self.request.session.pop('msg', False)
            if msg:
                messages.info(self.request, f'{msg}')
            return render(request, template_name=self.template_name, context={'form': form})

    def post(self, request, *args, **kwargs):
        """
        用户登录
        """
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        is_checked = int(request.POST.get('is_checked', '0'))

        # 登录
        user_obj = auth.authenticate(request, username=username, password=password)

        # 若验证失败,则跳转到登录界面
        if not user_obj:
            self.request.session['msg'] = '登陆失败，用户名或密码无效'
            return redirect('account:login')

        # 判断是否登录及是否需要保持登录状态
        if user_obj is not None and user_obj.is_active and is_checked:
            login(request, user_obj)

        # return render(request, 'account/index.html', context={'user': user_obj})
        return redirect('account:index')


class IndexView(View):
    """
    首页处理逻辑
    """
    template_name = "account/404.html"

    def get(self,  request, *args, **kwargs):
        user_obj = request.user

        # 判断用户是否登录
        if not user_obj.is_authenticated:
            return redirect(reverse("account:login"))

        return render(request, self.template_name, context={'user': user_obj})
