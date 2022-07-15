from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from .serializer import HelloSerializer


# Create your views here.
class HelloApiViewSet(viewsets.ModelViewSet):
    """
    多方法视图集合,提供增删改查
    list: 查询所有
    create: 创建数据
    """

    serializer_class = HelloSerializer
    queryset = []
    lookup_field = 'code'  # 指定主键名称,默认pk
    # lookup_url_kwarg = ('msg', 'code'),  # 查询单一数据时 URL 中的参数关键字名称，默认与 lookup_field 相同

    # 缓存下面的url地址
    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request, *args, **kwargs):
        """
        查询所有
        test
        :param request:
        :return:
        """
        # print(request.query_params)
        # print(request.version)
        data = {'code': 200, 'msg': 'hello word!', 'version': request.version}
        return Response(data)

    def create(self, request, *args, **kwargs):
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

    def retrieve(self, request, pk=None, *args, **kwargs):
        """
        查询
        :param request:
        :param pk:
        :return:
        """
        data = {'code': 200, 'msg': 'ok!'}
        return Response(data)

    def update(self, request, pk=None, *args, **kwargs):
        """
        更新
        :param request:
        :param pk: 记录主键
        :return:
        """
        data = {'code': 200, 'msg': 'ok!'}
        return Response(data)

    def partial_update(self, request, pk=None, *args, **kwargs):
        """
        部分更新
        :param request:
        :param pk: 记录主键
        :return:
        """
        data = {'code': 200, 'msg': 'ok!'}
        return Response(data)

    def destroy(self, request, pk=None, *args, **kwargs):
        """
        删除记录
        :param request:
        :param pk:
        :return:
        """
        data = {'code': 200, 'msg': 'ok!'}
        return Response(data)

    @action(['post', ], detail=False, url_path='latest', url_name='latest')
    def latest(self, request, *args, **kwargs):
        """
        获取最新一条数据
        :param request:
        :return:
        """
        data = {'code': 200, 'msg': 'ok!'}
        return Response(data)


class TestView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    自定义视图集合,单方法提供,并且需注册到api root视图示例,提供get查询
    """
    serializer_class = HelloSerializer
    queryset = []

    def list(self, request, *args, **kwargs):
        data = {'code': 200, 'msg': 'hello word!'}
        return Response(data)

    # detal: 是否需要使用主键来获取数据
    @action(['post', ], detail=False, url_path='latest', url_name='latest')
    def latest(self, request):
        """
        获取最新一条数据
        : param request:
        :return:
        """
        data = {'code': 200, 'msg': 'ok!'}
        return Response(data)

    @action(['get', ], detail=False, url_name='test', url_path=r'test/(?P<code>\w+)')
    def test(self, request, code=None, *args, **kwargs):
        """
        获取最新一条数据, 自定义url参数
        :param code:
        :param request:
        :return:
        """
        data = {'code': code, 'msg': 'ok!'}
        return Response(data)
