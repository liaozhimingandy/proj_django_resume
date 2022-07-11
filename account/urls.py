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
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    # url(r'^login/$', views.login, name='login'),
    # url(r'^logout/$', views.logout, name='logout'),
    # url(r'^profile/', views.ProfileView.as_view(), name='profile'),
    # url(r'^password_change/$', views.password_change, name='password_change'),
    # url(r'^password_change/done/$', views.password_change_done,
    #     name='password_change_done'),
    # url(r'^password_reset/$', views.password_reset, name='password_reset'),
    # url(r'^password_reset/done/$', views.password_reset_done,
    #     name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.reset, name='password_reset_confirm'),
    # url(r'^reset/done/$', views.reset_done, name='password_reset_complete'),

    # 用户登录api
    # re_path(r'^api/login/$', TokenObtainPairView.as_view(), name='login'),
    re_path(r'^api/login/$', views.MyTokenObtainPairView.as_view(), name='login'),
]

