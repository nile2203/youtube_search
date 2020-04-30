from _datetime import datetime
from django.db import models

# Create your models here.
from youtube_search.helper import get_24_char_uuid


class VideoDetails(models.Model):
    id = models.CharField(max_length=24, default=get_24_char_uuid, primary_key=True)
    thumbnail_url = models.URLField(max_length=2000)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(default=datetime.now)
    description = models.CharField(max_length=500)
    video_id = models.CharField(max_length=20, unique=True)
    platform = models.CharField(max_length=20)

    created = models.DateTimeField(default=datetime.now())

    def __unicode__(self):
        return '{} {}'.format(self.id, self.video_id)

    class Meta:
        verbose_name = 'Video Details'
        ordering = ['-published_date']


class YoutubeTokens(models.Model):
    keyword = models.CharField(max_length=50)
    page_token = models.CharField(max_length=10, unique=True)

    created = models.DateTimeField(default=datetime.now())

    def __unicode__(self):
        return '{} {}'.format(self.page_token, self.keyword)

    class Meta:
        verbose_name = 'Youtube page tokens'
        ordering = ['-created']
