from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema, no_body
from rest_framework.response import Response
from rest_framework import viewsets, generics

from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet, mixins

from .serializers import HelloApiSerializer


# Create your views here.
class HelloApiViewSet(viewsets.ModelViewSet):
    """
    get:
    返回所有图书信息.
    """

    # 参数配置
    code = openapi.Parameter('code', required=True, in_=openapi.IN_QUERY, description='仓库Id',
                             type=openapi.TYPE_STRING, default='test')

    # 编写以下内容
    serializer_class = HelloApiSerializer
    queryset = []

    def list(self, request):
        """
        :param request:
        :return:

        """
        # print(request.query_params)

        data = {'code': 200, 'msg': 'hello word!'}
        return Response(data)

    @swagger_auto_schema(
        request_body=HelloApiSerializer,
        operation_description='创建数据',
        responses={409: '已存在该数据', 401: '未认证', 400: openapi.Schema(type=openapi.TYPE_OBJECT,
                                                                  properties={
                                                                      'code': openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                                             description='错误代码',
                                                                                             default=404),
                                                                      'msg': openapi.Schema(type=openapi.TYPE_STRING,
                                                                                            description='错误描述',
                                                                                            default='未找到数据')})}
    )
    def create(self, request):
        # print(request.data)
        data = {'code': 200, 'msg': 'ok!'}
        return Response(data)

    @swagger_auto_schema(
        manual_parameters=[code],
        responses={
            '200': openapi.Response('', HelloApiSerializer)
        },
        security=[],
        operation_id=None,
        operation_description='查询一条数据',
    )
    def retrieve(self, request, pk=None):
        """
        查询
        :param request:
        :param pk:
        :return:
        """
        data = {'code': 200, 'msg': 'ok!'}
        return Response(data)

    @swagger_auto_schema(request_body=HelloApiSerializer, operation_id='no_body_test', responses={200: '更新成功!'})
    def update(self, request, pk=None):
        """
        更新
        """
        data = {'code': 200, 'msg': 'ok!'}
        return Response(data)

    @swagger_auto_schema(operation_description="partial_update description override", responses={404: 'slug not found'},
                         operation_summary='partial_update summary', deprecated=True)
    def partial_update(self, request, pk=None):
        """
        部分更新
        :param request:
        :param pk: 记录主键
        :return:
        """
        data = {'code': 200, 'msg': 'ok!'}
        return Response(data)

    def destroy(self, request, pk=None):
        """
        删除记录
        :param request:
        :param pk:
        :return:
        """
        data = {'code': 200, 'msg': 'ok!'}
        return Response(data)

    @action(['get', ], detail=False)
    def latest(self, request):
        """
        获取最新一条数据
        :param request:
        :return:
        """
        data = {'code': 200, 'msg': 'ok!'}
        return Response(data)

    @swagger_auto_schema(
        operation_id='hello_delete_bulk',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'data': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description='内容',
                    properties={'patient': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        description='患者信息',
                        items=(openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            description='内容',
                            properties={'patient_id': openapi.Schema(
                                type=openapi.TYPE_STRING,
                                description='患者id'
                            )}
                        ))
                    )}
                ),
                'id': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='id'
                ),
            },
            required=['id', ]
        ),
    )
    @action(['delete'], detail=False, url_path='delete_bulk')
    def delete(self, *args, **kwargs):
        """批量删除

        批量删除接口
        """
        pass

    @swagger_auto_schema(
        manual_parameters=[code],
        responses={
            200: HelloApiSerializer(many=True),
            404: openapi.Schema(type=openapi.TYPE_OBJECT,
                                properties={
                                    'code': openapi.Schema(type=openapi.TYPE_NUMBER,
                                                           description='错误代码', default=404),
                                    'msg': openapi.Schema(type=openapi.TYPE_STRING,
                                                          description='错误描述', default='未找到数据!')})
        },
        security=[],
        operation_id=None,
        operation_description='查询报告数据',
    )
    @action(['get'], detail=False, url_path='report')
    def report(self, *args, **kwargs):
        """
        查询报告数据
        """
        pass
