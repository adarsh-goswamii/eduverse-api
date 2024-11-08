from fastapi import APIRouter, Request, Response, Depends
from utils.auth import Auth
from services.auth.controller import TestController

router = APIRouter()

@router.get("/test")
@Auth.authenticate_user
@Auth.authorize_user
async def test(request: Request, payload: str):
  return await TestController.test(request, payload=payload)
