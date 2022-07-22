# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2022 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : zhiming
#   @Project     : proj_django_resume
#   @File Name   : serializer.py
#   @Created Date: 2022-07-07 14:28
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description :
#
# ======================================================================
from rest_framework import serializers

from .models import Hello


class HelloSerializer(serializers.Serializer):
    code = serializers.UUIDField(help_text='编码')
    msg = serializers.CharField(max_length=128, help_text='名称')

    def create(self, validated_data):
        return Hello(**validated_data)



