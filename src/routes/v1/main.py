from fastapi import APIRouter
from routes.v1 import test, video

api_router = APIRouter()

api_router.include_router(test.router, prefix='/v1/test', tags=["Test"])
api_router.include_router(video.router, prefix='/v1/video', tags=["Video"])
api_router.include_router(test.router, prefix='/v1/playlist', tags=["Playlist"])