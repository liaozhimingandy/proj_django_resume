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
from django.urls import re_path
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from .views import HelloApiViewSet

urlpatterns = [
    re_path(r'docs/', include_docs_urls(title="api接口文档")),
]

router = DefaultRouter()
router.register(r'v1/hello', HelloApiViewSet, basename='hello-api')
urlpatterns += router.urls
