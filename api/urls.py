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
from django.urls import re_path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.documentation import include_docs_urls
from .views import HelloApiViewSet, TestView

urlpatterns = [
    re_path(r'docs/', include_docs_urls(title="api接口文档", description='...')),
    re_path('api-auth/', include('rest_framework.urls', namespace='res_framework'))  # 认证地址
    # re_path('^test$', TestView.as_view(), name='test'),
]

router = DefaultRouter()
router.register(r'hello', HelloApiViewSet, basename='hello')
router.register(r'test', TestView, basename='test')
urlpatterns += router.urls
# print(router.urls)