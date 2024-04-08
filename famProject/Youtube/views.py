from django.shortcuts import render
from django.views.generic import View
from Youtube.serializers import YoutubeVideoListSerializer
from Youtube.models import YoutubeVideo
from django.db.models import Q
from django.http import HttpResponse
from Youtube.tasks import store_video_data
from famProject.constants import SUCCESS_RESPONSE
from famProject.response import init_response, send_200
import json
import requests


def home(request):
    return render(request, 'index.html')


def start_background_fetch(request):
    store_video_data.delay()
    return HttpResponse("Background fetch started.")


class YoutubeVideoList(View):

    def __init__(self):
        self.response = init_response()

    def get(self, request):
        params = request.GET
        limit = int(params.get("limit", 10))
        page = int(params.get("page", 1))
        title, description = params.get('title'), params.get('description')
        q1 = Q(title__icontains=title)
        q2 = Q(description__icontains=description)
        offset = (page-1) * limit
        if title and description:
            queryset = YoutubeVideo.objects.order_by('-published_at').filter(q1 | q2)[offset:offset+limit]
            total_count = YoutubeVideo.objects.filter(q1 | q2).count()
        elif title:
            queryset = YoutubeVideo.objects.order_by('-published_at').filter(q1)[offset:offset+limit]
            total_count = YoutubeVideo.objects.filter(q1).count()
        elif description:
            queryset = YoutubeVideo.objects.order_by('-published_at').filter(q2)[offset:offset+limit]
            total_count = YoutubeVideo.objects.filter(q2).count()
        else:
            queryset = YoutubeVideo.objects.order_by('-published_at').all()[offset:offset+limit]
            total_count = YoutubeVideo.objects.count()
        queryset = queryset.values(
            "channel_id",
            "video_id",
            "title",
            "description",
            "published_at",
            "thumbnail_default_url",
            "thumbnail_medium_url",
            "thumbnail_high_url"
        )
        result, count = YoutubeVideoListSerializer.serializer(queryset)
        self.response = {
            "res_str": SUCCESS_RESPONSE,
            "page": page,
            "count": count,
            "total_count": total_count,
            "res_data": result,
        }
        if page == 1:
            context = {'json': result, 'nextPage': page+1}
        else:
            context = {'json': result, 'nextPage': page+1, "prevPage": page-1}
        return render(request, 'index.html', context)



