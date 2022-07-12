
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from django.urls import reverse

from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.views import APIView
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

        headers = self.get_success_headers(serializer.data)
        print(ret_dict)
        return Response(ret_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


def Login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # 注意：验证用户名和密码是否正确放到forms中去验证了
            # login(request, request.user)  # 此处不能使用request.user,因为他还没有验证，是匿名用户
            # 所以需要在form中校验通过后传递过来user
            login(request, form.cleaned_data["user"])
            next_url = request.GET.get("next", reverse("index"))
            return redirect(next_url)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'account/login.html', context={'form': form})


def index(request):
    user = request.user
    return render(request, 'account/index.html', context={'user': user})



