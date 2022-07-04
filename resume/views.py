from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http.response import JsonResponse

from .models import BasicInfoModel, EducationModel, SkillModel, WorkExperienceModel


# Create your views here.
def hello(request):
    data = {'code': 200, 'msg': 'hello'}
    return JsonResponse(data)


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
                  context={'basic_info': basic_info, 'edu_infos': edu_infos,
                           'skill_infos': skill_infos, 'list_bg_color': list_bg_color,
                           'list_badge_color': list_badge_color, 'work_experiences': work_experiences})
