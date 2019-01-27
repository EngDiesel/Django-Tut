from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, This is the index page</h1>")


def get_album(request, album_id):
    return HttpResponse("<h1>Hello,This is <span style='color: red'>Album: " + str(album_id) + "</span></h1>")
