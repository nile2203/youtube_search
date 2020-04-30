from django.conf.urls import url

from youtube_search.videos import video_views

urlpatterns = [
    url(r'v1/video/search/task/?', video_views.api_initiate_youtube_search_task),
    url(r'v1/video/search/?', video_views.api_search_videos),
]