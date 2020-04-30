from django.db.models import Q

from youtube_search.helper import format_datetime_user_friendly
from youtube_search.models import YoutubeTokens, VideoDetails


class FampayVideoDetails:
    def __init__(self, video):
        self.video = video

    @staticmethod
    def set_page_token(page_token, keyword):
        YoutubeTokens.objects.create(keyword=keyword, page_token=page_token)

    @staticmethod
    def get_page_token(keyword):
        youtube_tokens = YoutubeTokens.objects.filter(keyword=keyword, id__gt=1)
        if not youtube_tokens:
            return None

        return youtube_tokens.first()

    @staticmethod
    def create_video_details(video_details):
        videos = []
        for video_detail in video_details:
            videos.append(VideoDetails(
                published_date=video_detail['published_date'],
                thumbnail_url=video_detail['thumbnail_url'],
                platform=video_detail['platform'],
                title=video_detail['title'],
                description=video_detail['description'],
                video_id=video_detail['video_id']
            ))

        try:
            return VideoDetails.objects.bulk_create(videos)
        except:
            return None

    @staticmethod
    def get_videos_by_query(query):
        return VideoDetails.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    @staticmethod
    def get_serialized_video_details(videos):
        serialized_videos = []
        for video in videos:
            serialized_videos.append({
                'id': video.id,
                'video_id': video.video_id,
                'published_date': format_datetime_user_friendly(video.published_date),
                'thumbnail_url': video.thumbnail_url,
                'title': video.title,
                'description': video.description
            })
        return serialized_videos
