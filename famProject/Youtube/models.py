from django.db import models

# Create your models here.


class YoutubeVideo(models.Model):
    channel_id = models.CharField(max_length=255, null=True, blank=True)
    video_id = models.CharField(max_length=255, db_index=True)
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    thumbnail_default_url = models.URLField(max_length=1000, null=True, blank=True)
    thumbnail_medium_url = models.URLField(max_length=1000, null=True, blank=True)
    thumbnail_high_url = models.URLField(max_length=1000, null=True, blank=True)