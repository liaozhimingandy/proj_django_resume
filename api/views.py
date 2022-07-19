from rest_framework.response import Response
from rest_framework import viewsets, generics

from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet, mixins

from .serializers import HelloApiSerializer
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
class HelloApiViewSet(viewsets.ViewSet):
    """
    get:
    返回所有图书信息.
    """
    # 编写以下内容
    serializer_class = HelloApiSerializer

    @swagger_auto_schema(operation_description="partial_update description override",
                         responses={'404': 'id not found'})
    def list(self, request):
        """
        :param request:
        :return:

        """
        # print(request.query_params)

        data = {'code': 200, 'msg': 'hello word!'}
        return Response(data)

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

    def retrieve(self, request, pk=None):
        """
        查询
        :param request:
        :param pk:
        :return:
        """
        data = {'code': 200, 'msg': 'ok!'}
        return Response(data)

    def update(self, request, pk=None):
        """
        更新
        :param request:
        :param pk: 记录主键
        :return:
        """
        data = {'code': 200, 'msg': 'ok!'}
        return Response(data)

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
