from fastapi import Request
from functools import wraps

class Auth:
  @classmethod
  def authenticate_user(cls, func):
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
      """
      Authenticate user
      """
      print("You are authenticated")
      return await func(request, *args, **kwargs)
    
    return wrapper

  @classmethod
  def authorize_user(cls, func):
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
      """
      Authorize user
      """
      print("You are authorized")
      return await func(request, *args, **kwargs)
    
    return wrapper