# -*- encoding: utf-8 -*-
'''
@文件        :views.py
@说明        :
@时间        :2022/02/03 19:51:45
@作者        :misldy.top
'''
import os
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')


def load(request):
    nowdir = os.getcwd()
    try:
        flag = str(request.GET.get('flag'))
        path = nowdir + "/templates"
        os.chdir(path)
        filename = flag + ".html"
        f = open(file=filename, mode="rb")
        data = f.read()
        resp = HttpResponse(data, content_type='application/vnd.ms-excel')
        # 通过响应头告知浏览器下载该文件以及对应的文件名
        resp['content-disposition'] = f'attachment; filename*=utf-8\'\'{filename}'
        # return resp
        print(resp)
        return render(request, 'index.html')

    except Exception:
        data = {'code': 30001, 'msg': '加载模板失败'}
        return JsonResponse(data)
    finally:
        os.chdir(nowdir)
