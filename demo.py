from django.http import HttpResponse


def index(request):
    print("161牛逼")

    return HttpResponse('上面说的是假的')


def login(request):

    print("这是登陆视图")

    return HttpResponse()