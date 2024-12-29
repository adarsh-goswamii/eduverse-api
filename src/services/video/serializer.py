from pydantic import BaseModel
from typing import Optional, List

class UploadYoutubeVideoInbound(BaseModel):
  title: str
  description: Optional[str] = ""
  raw_video_url: str
  playlist_id: Optional[int] = None
  tags: Optional[List[int]] = []
  
class GetYoutubeVideoDetailsOutbound(BaseModel):
  title: str
  description: Optional[str] = ""
  thumbnail_url:  Optional[str] = ""
  duration: Optional[int] = 0
    
class YoutubeVideoThumbnail(BaseModel):
  url: str
  width: int
  height: int
  
class YoutubeVideoThumbnails(BaseModel):
  default: Optional[YoutubeVideoThumbnail]
  medium: Optional[YoutubeVideoThumbnail]
  high: Optional[YoutubeVideoThumbnail]
  standard: Optional[YoutubeVideoThumbnail]
  maxres: Optional[YoutubeVideoThumbnail]

class YoutubeVideoContentDetails:
  duration: str

class YoutubeVideoSnippet(BaseModel):
  publishedAt: str
  title: str
  description: str
  thumbnails: YoutubeVideoThumbnails
    
class YoutubeVideoDetail(BaseModel):
  kind: str
  etag: str
  id: str
  snippet: YoutubeVideoSnippet
  contentDetails: YoutubeVideoContentDetails
  
class PageInfo(BaseModel):
  totalResults: int
  resultsPerPage: int
    
class GetYoutubeVideosDetails(BaseModel):
  kind: str
  etag: str
  items: List[YoutubeVideoDetail]
  pageInfo: PageInfo