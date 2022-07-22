from collections import OrderedDict
from itertools import chain

from django.contrib.admin.utils import label_for_field, display_for_field
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views import View
from django.views.generic import UpdateView, DetailView
from django.apps import apps

from .models import BasicInfoModel, EducationModel, SkillModel, WorkExperienceModel


# Create your views here.
def show(request, user):
    basic_info = get_object_or_404(BasicInfoModel, user_id=user)
    edu_infos = get_list_or_404(EducationModel, resume_id=basic_info.id)
    edu_infos = sorted(edu_infos, key=lambda x: x.gmt_education_end, reverse=True)

    skill_infos = get_list_or_404(SkillModel, resume_id=basic_info.id)
    skill_infos = sorted(skill_infos, key=lambda value: value.skill_level, reverse=True)

    work_experiences = get_list_or_404(WorkExperienceModel, resume_id=basic_info.id)
    work_experiences = sorted(work_experiences, key=lambda value: value.gmt_duration, reverse=True)

    list_bg_color = ['bg-success', 'bg-info', 'bg-warning', 'bg-danger', 'bg-primary', 'bg-secondary', 'bg-dark']
    list_badge_color = ['badge-info', 'badge-primary', 'badge-light', 'badge-success', 'badge-danger',
                        'badge-secondary', 'badge-warning', 'badge-dark']

    return render(request, 'resume/resume.html',
                  context={'basicinfo': basic_info, 'edu_infos': edu_infos,
                           'skill_infos': skill_infos, 'list_bg_color': list_bg_color,
                           'list_badge_color': list_badge_color, 'work_experiences': work_experiences})


class IndexView(View):
    """
    首页处理逻辑
    """
    template_name = "resume/index.html"

    def get(self, request, *args, **kwargs):
        user_obj = request.user
        # 判断用户是否登录
        if not user_obj.is_authenticated:
            return redirect(reverse("account:login"))

        return render(request, self.template_name, context={'user': user_obj})


class BasicInfoUpdate(UpdateView):
    template_name = 'resume/basicinfo/update.html'
    model = BasicInfoModel
    fields = ['name_cn', 'name_en']
    context_object_name = 'obj'


class DetailModelView(DetailView):
    """
    获取模型详细数据通用视图,多个模型均可使用
    """
    context_object_name = 'obj'

    def get_template_names(self):
        template_name = f"resume/{self.kwargs.get('model', '')}/detail.html"
        return template_name

    def dispatch(self, request, *args, **kwargs):
        # parse param from url
        _model = self.kwargs.get('model', '') + 'model'
        self.model = apps.get_model('resume', _model.lower())
        self.pk_url_kwarg = self.kwargs.get('pk', '')
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.pk_url_kwarg)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _extra = {
            'obj':  self.get_object(),
            'obj_as_table': self.make_info_panel
        }
        context.update(**_extra)
        self.field_for_model()
        return context

    @property
    def make_info_panel(self):
        """
        动态转换字段,将字段转成html标签
        :return:
        """
        exclude = [
            'id', 'password', 'user_permissions', 'deleted', 'mark'
        ]

        base_field = self.field_for_model()
        fields = [f for f in base_field]
        default_fields = getattr(self.model._meta, 'list_display', None)
        if default_fields and isinstance(default_fields, list):
            o = [f for f in fields if f not in default_fields]
            default_fields.extend(o)
            fields = default_fields
        panel = ''
        for index, field_name in enumerate(fields, 1):
            tr_format = '<tr><th>{th}</th><td>{td}</td>'
            th = label_for_field(name=field_name, model=self.model)

            field = self.model._meta.get_field(field_name)
            value = field.value_from_object(self.object)
            value_field = display_for_field(value, field, empty_value_display=False)

            tr_html = tr_format.format(th=th, td=value_field)
            panel += tr_html

        return mark_safe(panel)

    def field_for_model(self, fields=None, exclude=None):
        field_list = []
        opts = self.model._meta
        for f in chain(opts.concrete_fields, opts.many_to_many):
            if fields and f.name not in fields:
                continue
            if exclude and f.name in exclude:
                continue
            else:
                field_list.append((f.name, f))
        field_dict = OrderedDict(field_list)
        return field_dict







