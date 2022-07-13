"""
Django settings for proj_django_resume project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "SECRET_KEY", "django-insecure-=nk4852m0)81-)-54(9dr-_%w@-oowoobqh(7n60+hw$139_1u"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG", default=1))
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "*").split(" ")

CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "http://*").split(" ")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'coreapi',
    'rest_framework',
    'django_filters',
    'ckeditor',  # 富文本编辑器

    'resume',  # 自定义app
    'api',
    'account',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proj_django_resume.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

        },
    },
]

WSGI_APPLICATION = 'proj_django_resume.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'assets/db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 富文本编辑器配置
CKEDITOR_CONFIGS = {
    'default': {
        # 使用简体中文
        'language': 'zh-cn',
        'toolbar': 'full',  # 工具条功能
        'height': 300,  # 编辑器高度
        'width': 'auto',  # 编辑器宽
    },
}
CKEDITOR_UPLOAD_PATH = ''  # 上传图片保存路径，留空则调用django的文件上传功能

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
# static目录配置
STATIC_URL = 'static/'

# python manage.py collectstatic 收集文件到下面文件文件夹里
STATIC_ROOT = os.path.join(BASE_DIR, "assets")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# drf配置
REST_FRAMEWORK = {
    # 5.分页设置
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    # 指定过滤后端
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend', ],
    # 渲染器
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
    ),
    # 指定用于支持coreapi的Schema
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema',
    'DEFAULT_THROTTLE_CLASSES': (  # 定义限流类
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    # 3.定义限流速率（支持天数/时/分/秒的限制）
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/m',
        'user': '60/m',
    },

    # 异常处理
    # 'EXCEPTION_HANDLER': 'luffy.utils.exceptions.custom_exception_handler',

    # 5.1过滤排序（全局）：Filtering 过滤排序
    'SEARCH_PARAM': 'search',
    'ORDERING_PARAM': 'ordering',

    # 1.定义认证配置
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # jwt认证
        # 'rest_framework.authentication.BasicAuthentication',  # 基本认证
        # 'rest_framework.authentication.SessionAuthentication',  # session认证 drf测试时需要用上
    ),
    # 2.默认权限设置
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAdminUser',  # 管理员可以访问
        # 'rest_framework.permissions.IsAuthenticated',  # 认证用户可以访问
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',  # 认证用户可以访问, 否则只能读取 authentication: Bearer [token]访问接口
        # 'rest_framework.permissions.AllowAny',  # 所有用户都可以访问
    ),
    # Schemas
    'SCHEMA_COERCE_PATH_PK': True,
    'SCHEMA_COERCE_METHOD_NAMES': {
        'retrieve': 'read',
        'destroy': 'delete'
    },

    # 6.全局版本控制：Versioning  接口版本控制;
    # 请求头携带eg: Accept: application/json; version=1.0
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.AcceptHeaderVersioning",  # 类的路径
    'DEFAULT_VERSION': 'v1',  # 默认的版本
    'ALLOWED_VERSIONS': ['v1', 'v2'],  # 允许的版本
    'VERSION_PARAM': 'version',
}

# jwt载荷中的有效期设置
# 用法： https://zhuanlan.zhihu.com/p/339409769
SIMPLE_JWT = {
    # 过期时间
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=15),
    # 允许刷新
    'ROTATE_REFRESH_TOKENS': True,
    # 刷新的过期时间
    'JWT_REFRESH_EXOIRATION_DELTA': timedelta(days=2),
    'JWT_EXPIRATION_DELTA': timedelta(seconds=300),  # 设置 JWT Token 的有效时间
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'ALGORITHM': 'HS256',
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
}
# 自定义用户模型
AUTH_USER_MODEL = "account.UserProfile"
