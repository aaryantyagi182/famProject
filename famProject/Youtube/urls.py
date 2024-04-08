from django.urls import re_path as url
from Youtube import views

urlpatterns = [
    url(r'^v1/youtube/video/list/$', views.YoutubeVideoList.as_view(), name='youtube-search'),
]
