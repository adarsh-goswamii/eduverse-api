from fastapi import Request
from src.lib.redis import redis_cache
from src.configs.redis_constants import RedisExpInSec, RedisKey
from src.services.video.serializer import (
    UploadYoutubeVideoInbound,
    GetYoutubeVideoDetailsOutbound,
    GetYoutubeVideosDetails,
)
from src.lib.api import api
from src.configs.constants import GoogleApis
from src.configs.env import get_settings
from src.utils.datetime import datetime

config = get_settings()


class VideoController:
    """Video Controller"""

    @classmethod
    async def upload_youtube_video(
        self, request: Request, payload: UploadYoutubeVideoInbound
    ):
        return payload

    @classmethod
    async def get_youtube_video_details(self, request: Request, id: str):
        param = {
            "part": "snippet,contentDetails,statistics",
            "id": id,
            "key": config.google_api_key,
        }
        url = f"{GoogleApis.BASE_URL}{GoogleApis.GET_VIDEO_LIST}"
        print(url)
        response: GetYoutubeVideosDetails = await api.async_get_request(
            url=url, params=param
        )
        # create custom exception
        if response.get("pageInfo", {}).get("totalResults", 0) == 0:
            return response

        video_details = response.get("items", [])[0]
        thumbnail_url, resolution = "", 0

        thumbnails = video_details.get("snippet", {}).get("thumbnails", {})
        for key in thumbnails:
            if resolution < thumbnails.get(key, {}).get("width", 0):
                thumbnail_url = thumbnails.get(key, {}).get("url", "")
                resolution = thumbnails.get(key, {}).get("width", 0)

        data = (
            GetYoutubeVideoDetailsOutbound(
                title=video_details.get("snippet", {}).get("title", ""),
                description=video_details.get("snippet", {}).get("description", ""),
                thumbnail_url=thumbnail_url,
                duration=datetime.iso8601_to_seconds(
                    video_details.get("contentDetails", {}).get("duration", "")
                ),
            ),
        )

        print("hii")
        return data
