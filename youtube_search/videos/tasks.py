from googleapiclient.discovery import build

from fampay.settings import YOUTUBE_DEVELOPER_KEY
from youtube_search.celery import app

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def get_youtube_service():
    youtube_service = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                            developerKey=YOUTUBE_DEVELOPER_KEY)
    return youtube_service


def get_video_details_from_response(response):
    video_details = list()
    videos = response.get('items')
    if not videos:
        return None

    for video in videos:
        video_snippet = video['snippet']
        video_detail = {
            'published_date': video_snippet['publishedAt'],
            'title': video_snippet['title'],
            'description': video_snippet['description'],
            'video_id': video['id']['videoId'],
            'thumbnail_url': video_snippet['thumbnails']['medium']['url'],
            'platform': YOUTUBE_API_SERVICE_NAME.title()
        }
        video_details.append(video_detail)

    return video_details


@app.task
def get_youtube_video_details(query, max_results=25):
    youtube_service = get_youtube_service()
    response = youtube_service.search().list(q=query, part='snippet', maxResults=max_results, type='video').execute()

    result = {
        'videos': get_video_details_from_response(response),
        'page_token': response['nextPageToken']
    }
    return result


@app.task
def get_youtube_video_details_with_page_token(result, query, max_results=25):
    if not (isinstance(result, dict) and result):
        return None

    page_token = result['page_token']
    youtube_service = get_youtube_service()
    response = youtube_service.search().list(q=query, part='snippet', maxResults=max_results, type='video',
                                             pageToken=page_token).execute()

    result = {
        'videos': get_video_details_from_response(response),
        'page_token': response['nextPageToken']
    }
    return result

