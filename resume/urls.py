# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2022 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : zhiming
#   @Project     : proj_django_resume
#   @File Name   : urls.py
#   @Created Date: 2022-06-23 22:47
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description : app内部url
#
# ======================================================================
from django.urls import path, re_path
from .views import hello, show, IndexView, BasicInfoUpdate

app_name = 'resume'

urlpatterns = [
    # re_path(r'^$', hello, name='hello'),
    re_path(r'show/(?P<user>\w+)/', show, name='show-resume'),
    re_path('^$', IndexView.as_view(), name='index'),
    path('basicinfo/<int:pk>/', BasicInfoUpdate.as_view(), name='basicinfo-update'),
]
