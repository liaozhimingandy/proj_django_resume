# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2022 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : liaoz
#   @Project     : proj_django_resume
#   @File Name   : serializers.py
#   @Created Date: 2022-07-05 10:32
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description :
#
# ======================================================================
from rest_framework import serializers
from .models import Hello


class HelloApiSerializer(serializers.Serializer):
    id = serializers.UUIDField(help_text='记录主键')
    code = serializers.CharField(max_length=10, help_text='代码')
    msg = serializers.CharField(max_length=128, help_text='描述')

    def create(self, validated_data):
        return Hello(**validated_data)
