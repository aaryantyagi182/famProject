from celery import shared_task
from .utils import fetch_and_store_youtube_videos
from time import sleep


@shared_task
def store_video_data():
    while True:
        fetch_and_store_youtube_videos()
        sleep(10)  # adjust the interval as needed
