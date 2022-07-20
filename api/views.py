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
        operation_description='创建数据'
    )
    def create(self, request):
        """
        # 实现备注:
        **获取项目列表信息**<br><br>
        # 参数信息
        |  请求参数    |  类型 |  说明   |  是否必填    |   附加信息 |
        | ---- | ---- | ---- | ---- | ---- |
        |   name   |   string   | 项目名称 |    N |   无  |
        |   page   |  int    |   页数  |  Y  |  无  |
        |   page_size   |  int    |  每页容量  |  N   |  page_size=[10,20,50,100] |

        |  响应参数    |  类型 |  说明    |
        | ---- | ---- | ---- |
        |   code   |   int   | 响应结果码  |
        |   msg   |  string    |   响应结果信息  |
        |   data   |  JSON    |  返回数据   |

        ## 响应code说明
        |  Code    |  Description    |
        | ---- | ---- |
        |   0   |   成功   |
        |   10000   |  参数非法    |
        | 10004 | 获取数据失败 |

        parameters:
          - name: name
            type: string
            required: true
            location: form
        # 示例:
        ## request:
                - body:
                    Example value:
                    {
                        'name': 'publishSystem',
                        'page': 1,
                        'page_size': 10
                    }

        ## response:
                - body:
                     Example value:
                     {
                        "code": 0,
                        "msg": "\u6210\u529f",
                        "data": {
                            "list": [{
                                        "id": 2,
                                        "name": "publishSystem",
                                        "desc": "-",
                                        "status": true,
                                        "create_time": "2019-10-25 10:52:50",
                                        "modify_time": "2019-10-25 11:31:32",
                                        "is_delete": false
                                    }],
                            "count": 1
                        }
                    }


          ##  responses:
                400:
                  description: "Invalid ID supplied"
                404:
                  description: "Pet not found"
                405:
                  description: "Validation exception"""

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
