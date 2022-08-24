"""xwp_misldy_top URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'xwp_misldy_top'

urlpatterns = [
    path('admin/', admin.site.urls),
    # 添加用户管理访问路径
    path('usermgt/', include("usermgt.urls", namespace='usermgt')),
    # 添加网站首页
    path('', views.index, name='index'),
    # 添加tools平台
    path('tools/', include('tools.urls', namespace='tools')),
    # 123
    path('load/', views.load),
    # 456
    # path('load/?flag=index', views.index, name='index')
]
