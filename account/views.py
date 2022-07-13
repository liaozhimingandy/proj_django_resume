from coreapi.auth import SessionAuthentication
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, update_session_auth_hash, logout
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

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


@method_decorator(csrf_exempt, name='dispatch')
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
        data = request.data
        ser = self.get_serializer(data=data)
        ser.is_valid(raise_exception=True)

        username = ser.vaild_data.get('username', '')
        password = ser.vaild_data.get('password')
        user_obj = auth.authenticate(request, username=username, password=password)

        return Response('成功')


def index(request):
    user = request.user
    return render(request, 'account/index.html', context={'user': user})


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
    template_name = "account/login.html"

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, template_name=self.template_name, context={'form': form})

    def post(self, request, *args, **kwargs):
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # 注意：验证用户名和密码是否正确放到forms中去验证了
            # login(request, request.user)  # 此处不能使用request.user,因为他还没有验证，是匿名用户
            # 所以需要在form中校验通过后传递过来user
            login(request, form.cleaned_data["user"])
            next_url = request.GET.get("next", reverse("account:index"))
            return redirect(next_url)
        else:
            form = LoginForm()
            return render(request, template_name=self.template_name, context={'form': form})

