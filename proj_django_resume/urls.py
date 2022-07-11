"""proj_django_resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    re_path('api-auth/', include('rest_framework.urls', namespace='res_framework')),  # 认证地址
    re_path(r'docs/', include_docs_urls(title="api接口文档", description='...')),
    path('admin/', admin.site.urls),
    path('resume/', include('resume.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path('api/', include('api.urls')),
    re_path('account/', include('account.urls')),
]
#
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()