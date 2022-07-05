from rest_framework.response import Response
from rest_framework import viewsets, generics

from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet, mixins

from .serializers import HelloApiSerializer


# Create your views here.
class HelloApiViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    get:
    返回所有图书信息.
    """
    # 编写以下内容
    serializer_class = HelloApiSerializer

    def list(self, request):
        """
        查询所有数据
        """
        # print(request.query_params)

        data = {'code': 200, 'msg': 'hello word!'}
        return Response(data)

    def create(self, request):
        """
        创建数据
        :param request:
        :param page: 页数
        :return:
        """
        # print(request.data)
        serializer_class = HelloApiSerializer
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
