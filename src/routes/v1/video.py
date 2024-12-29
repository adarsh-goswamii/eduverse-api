from fastapi import APIRouter, Request, Response, Depends
from utils.auth import Auth
from services.video.controller import VideoController

router = APIRouter()

@router.get("/link-upload")
@Auth.authenticate_user
@Auth.authorize_user
async def video(request: Request, payload: str):
  return await VideoController.upload_youtube_video(request, payload=payload)

@router.get("/youtube/details/{id}")
@Auth.authenticate_user
@Auth.authorize_user
async def video(request: Request, id: str):
  return await VideoController.get_youtube_video_details(request, id)
