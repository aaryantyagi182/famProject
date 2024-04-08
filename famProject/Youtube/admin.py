from django.contrib import admin
from Youtube.models import YoutubeVideo


class YoutubeVideoAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(YoutubeVideo, YoutubeVideoAdmin)
