# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2022 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : zhiming
#   @Project     : proj_django_resume
#   @File Name   : forms.py
#   @Created Date: 2022-07-12 6:43
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description :
#
# ======================================================================
from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        min_length=3,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "请输入用户名"}),
        error_messages={
            "required": "用户名不能为空",
            "min_length": "用户名最小长度为3位",
        },
    )
    password = forms.CharField(
        label="密码",
        min_length=6,
        error_messages={
            "min_length": "密码最小长度为6位",
            "required": "密码不能为空",
        },
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "请输入密码"}),
    )

    def clean(self):
        username = self.cleaned_data.get("username", "")
        password = self.cleaned_data.get("password", "")
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("用户名或密码错误")

        self.cleaned_data["user"] = user
        return self.cleaned_data


class RegisterForm(LoginForm):
    password_again = forms.CharField(
        label="确认密码",
        min_length=6,
        error_messages={
            "required": "确认密码不能为空",
            "min_length": "密码最小长度为6位",
        },
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "确认密码"}),
    )
    email = forms.EmailField(
        label="邮箱",
        required=False,
        error_messages={
            "required": "密码不能为空",
        },
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "请输入邮箱"})
    )

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("用户名已存在")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("邮箱已存在")

        return email

    def clean(self):
        password = self.cleaned_data.get("password", "")
        password_again = self.cleaned_data.get("password_again", "")

        if password != password_again:
            raise forms.ValidationError("两次密码不一致，请重新输入")

        return self.cleaned_data

