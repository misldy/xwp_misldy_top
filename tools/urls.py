# -*- coding:utf-8 -*-
# author: SM0558
# datetime: 2021/4/26 09:33
# software: PyCharm
from django.urls import path

from . import views

app_name = 'tools'
urlpatterns = [
    path('', views.index, name='index'),
    path('json', views.json_base, name='json'),
    path('json_to_xml', views.json_to_xml, name='json_to_xml'),
    path('json_to_yaml', views.json_to_yaml, name='json_to_yaml'),
    path('json_to_go', views.json_to_go, name='json_to_go'),
    path('base64', views.base64_base, name='base64'),
    path('image_to_base64', views.image_to_base64, name='image_to_base64'),
    path('timestamp', views.timestamp_html, name='timestamp'),
    path('color', views.color_html, name='color'),
    path('number', views.number_html, name='number'),
    path('url', views.url_html, name='url'),
    path('unicode', views.unicode_html, name='unicode'),
    path('pdf2img', views.pdf2img_html, name='pdf2img'),
    path('morse', views.morse_html, name='morse'),
    path('hash', views.hash_html, name='hash'),
    path('file_hash', views.file_hash, name='file_hash'),
    path('aes', views.aes_html, name='aes'),
    path('des', views.des_html, name='des'),
    path('rsa', views.rsa_html, name='rsa'),
    path('tinyimg', views.tinyimg, name='tinyimg'),
    path('qrcode', views.qrcode, name='qrcode'),
    path('regex', views.regex_html, name='regex'),
    path('websocket', views.websocket, name='websocket')
]
