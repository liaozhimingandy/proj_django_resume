from django.shortcuts import render
from django.contrib import auth

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Create your views here.
class Login(APIView):
    """用户登录接口"""

    def post(self, request, verison=None):

        # 1. 获取到表单的数据
        req_data = request.data
        username = request.data.get('username')
        password = request.data.get('password')

        data = {'code': 200, 'msg': 'success'}
        # 2.校验用户
        user_obj = auth.authenticate(request, username=username, password=password)
        if user_obj:
            # payload = jwt_payload_handler(user_obj)
            # token = jwt_encode_handler(payload)
            user_data = {'username': user_obj.username, 'token': token, }
            data['data'] = user_data
        else:
            data['code'] = 400
            data['msg'] = '账号或密码错误'

        return Response(data)


