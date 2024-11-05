from fastapi import APIRouter, Request, Response, Depends
from utils.auth import Auth
from services.auth.controller import AuthController

router = APIRouter()

@router.get("/login")
@Auth.authenticate_user
@Auth.authorize_user
async def login_user(request: Request, payload: str):
  return await AuthController.login(request, payload=payload)
