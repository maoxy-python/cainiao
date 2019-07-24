from django.http import HttpResponse


def index(request):
    print("161牛逼")

    return HttpResponse('上面说的是假的')