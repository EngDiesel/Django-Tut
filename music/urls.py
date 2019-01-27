# from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # /music/
    path('', views.index, name="index"),

    # /music/<int:album_id>
    path('<int:album_id>/', views.get_album, name='album'),
]
