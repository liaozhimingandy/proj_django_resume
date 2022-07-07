from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action

from .serializer import HelloSerializer
from .models import Hello


# Create your views here.
class HelloApiViewSet(viewsets.ModelViewSet):
    """
    多方法视图集合,提供增删改查
    list: 查询所有
    create: 创建数据
    """

    serializer_class = HelloSerializer
    queryset = []

    def list(self, request):
        """
        查询所有
        test
        :param request:
        :return:
        """
        # print(request.query_params)
        data = {'code': 200, 'msg': 'hello word!'}
        return Response(data)

    def create(self, request):
        """
        创建数据
        :param request:
        :return:
        """
        # print(request.data)
        data = {'code': 200, 'msg': 'ok!'}
        ser = HelloSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        data = ser.validated_data
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


class TestView(mixins.ListModelMixin, viewsets.ViewSet):
    """
    自定义视图集合,单方法提供,并且需注册到api root视图示例,提供get查询
    """

    def list(self, request, *args, **kwargs):
        data = {'code': 200, 'msg': 'hello word!'}
        return Response(data)
