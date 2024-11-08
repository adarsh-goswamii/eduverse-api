from fastapi import APIRouter
from routes.v1 import test

api_router = APIRouter()

api_router.include_router(test.router, prefix='/v1/test', tags=["Test"])