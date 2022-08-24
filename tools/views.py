from django.shortcuts import render


def index(request):
    return render(request, 'tools/index.html')


def json_base(request):
    return render(request, 'tools/json.html')


def json_to_xml(request):
    return render(request, 'tools/json2xml.html')


def json_to_yaml(request):
    return render(request, 'tools/json2yaml.html')


def json_to_go(request):
    return render(request, 'tools/json2go.html')


def json_html(request):
    return render(request, 'tools/json.html')


def base64_base(request):
    return render(request, 'tools/base64.html')


def image_to_base64(request):
    return render(request, 'tools/image2base64.html')


def timestamp_html(request):
    return render(request, 'tools/timestamp.html')


def color_html(request):
    return render(request, 'tools/color.html')


def number_html(request):
    return render(request, 'tools/number.html')


def url_html(request):
    return render(request, 'tools/url.html')


def unicode_html(request):
    return render(request, 'tools/unicode.html')


def pdf2img_html(request):
    return render(request, 'tools/pdf2img.html')


def morse_html(request):
    return render(request, 'tools/morse.html')


def hash_html(request):
    return render(request, 'tools/hash.html')


def file_hash(request):
    return render(request, 'tools/file_hash.html')


def aes_html(request):
    return render(request, 'tools/aes.html')


def des_html(request):
    return render(request, 'tools/des.html')


def rsa_html(request):
    return render(request, 'tools/rsa.html')


def tinyimg(request):
    return render(request, 'tools/tinyimg.html')


def qrcode(request):
    return render(request, 'tools/qrcode.html')


def regex_html(request):
    return render(request, 'tools/regex.html')


def websocket(request):
    return render(request, 'tools/websocket.html')
