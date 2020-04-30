from rest_framework.decorators import api_view

from youtube_search.paginator import FampayPaginator
from youtube_search.result_builder import ResultBuilder
from youtube_search.videos.tasks import get_and_create_youtube_video_details
from youtube_search.videos.videos import FampayVideoDetails


@api_view(['POST'])
def api_initiate_youtube_search_task(request):
    result_builder = ResultBuilder()
    post_data = request.data

    query = post_data.get('query')
    if not query:
        return result_builder.fail().bad_request_400().message('No query provided').get_response()

    get_and_create_youtube_video_details.apply_async([query], countdown=30)
    return result_builder.ok_200().success().message('Initiated data pull from youtube').get_response()


@api_view(['GET'])
def api_search_videos(request):
    result_builder = ResultBuilder()
    get_data = request.GET

    page_number = get_data.get('page', 1)
    search_query = get_data.get('query')
    if not search_query:
        return result_builder.fail().bad_request_400().message('No query provided').get_response()

    videos = FampayVideoDetails.get_videos_by_query(search_query)
    if not videos:
        return result_builder.fail().ok_200().message('No query provided').get_response()

    fp_paginator = FampayPaginator(data=videos, page_size=25)
    status, message, videos = fp_paginator.get_page(page_number)
    if status == 0:
        return result_builder.fail().ok_200().message(message).get_response()

    serialized_video_details = FampayVideoDetails.get_serialized_video_details(videos)
    result = {
        'videos': serialized_video_details
    }
    return result_builder.success().ok_200().message('Video details fetched').result_object(result).get_response()
