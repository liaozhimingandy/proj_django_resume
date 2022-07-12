# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2022 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : zhiming
#   @Project     : proj_django_resume
#   @File Name   : serializers.py
#   @Created Date: 2022-07-11 8:14
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description :
#
# ======================================================================
from abc import ABC

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from .models import UserProfile


class AccountTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        """此方法往token的有效负载
        payload
        里面添加数据
        若自定义了用户表，可以在这里面添加用户邮箱，性别，年龄等可以公开的信息
        这部分放在token里面是可以被解析的，所以不要放比较私密的信息"""
        token = super().get_token(user)
        token['name'] = user.username
        return token

    def validate(self, attrs):
        """
         此方法是 响应数据结构，默认返回只有 access 和 refresh
         :param attrs:
         :return:
        """
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        # print(refresh.access_token.payload)
        # 令牌到期时间
        data['expire'] = refresh.access_token.payload['exp']  # 有效期
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['token'] = str(refresh.access_token)
        data['username'] = self.user.username
        return data


class UserRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'name']