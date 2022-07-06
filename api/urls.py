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
from django.shortcuts import redirect
from django.urls import re_path, path
from .views import HelloApiViewSet

from rest_framework import routers
from rest_framework.decorators import api_view
# 使用drf提供的路由类来自动生成路由
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# router 的作用就是自动生成 Api Root 页面
router = DefaultRouter()  # 可以处理视图的路由器
router.register('v1/hello', HelloApiViewSet, basename="hello")  # 向路由器中注册视图集,"user":浏览器访问的路径，basename:路由别名
# router.register('DemoAPIView', DemoAPIView, basename="demo")
urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中
