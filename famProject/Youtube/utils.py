from Youtube.constants import API_KEY, SEARCH_API, API_KEY_2
from datetime import datetime
from famProject.network import network_call
from famProject.constants import GET, POST
from Youtube.models import YoutubeVideo


def fetch_and_store_youtube_videos():
    params = {
        "key": API_KEY,
        "publishedAfter": datetime.now().date().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "maxResults": 20,
        "order": "date",
        "part": "snippet",
        "type": "video",
        "q": "cricket"
    }
    data = network_call(url=SEARCH_API, method=GET, params=params, headers={})
    if not data:
        params["key"] = API_KEY_2
        data = network_call(url=SEARCH_API, method=GET, params=params, headers={})

    for item in data["items"]:
        video_id = item["id"]["videoId"]
        title = item["snippet"]["title"]
        description = item["snippet"]["description"]
        published_at = item["snippet"]["publishedAt"]
        channel_id = item["snippet"]["channelId"]
        thumbnail_default_url = item["snippet"]["thumbnails"]["default"]["url"]
        thumbnail_medium_url = item["snippet"]["thumbnails"]["medium"]["url"]
        thumbnail_high_url = item["snippet"]["thumbnails"]["high"]["url"]

        # Convert published_at to datetime object
        published_at = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")

        # Check if the video already exists in the database
        if not YoutubeVideo.objects.filter(video_id=video_id).exists():
            print("Does not exist so creating a new")
            YoutubeVideo.objects.create(
                video_id=video_id,
                channel_id=channel_id,
                title=title,
                description=description,
                published_at=published_at,
                thumbnail_default_url=thumbnail_default_url,
                thumbnail_medium_url=thumbnail_medium_url,
                thumbnail_high_url=thumbnail_high_url
            ).save()
