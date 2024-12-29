import httpx
import logging
from src.configs.error_constants import ErrorMessages

logger = logging.getLogger()

class Api:
  async def async_get_request(self, url: str, headers: dict = None, params: dict = None):
    print(url)
    async with httpx.AsyncClient() as client:
      try:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
      
      except httpx.RequestError as exc:
        # This will catch any network-related errors (e.g., DNS lookup failure, connection error)
        logger.exception(f"{ErrorMessages.NETWORK_ERROR}: {exc}")
        raise 
    
      except httpx.HTTPStatusError as exc:
        # This will catch HTTP errors like 4xx or 5xx responses
        logger.exception(f"{ErrorMessages.HTTP_ERROR}: {exc}")
        raise 
      
      except Exception as exc:
        # Catch all other exceptions
        logger.exception(f"{ErrorMessages.GENERIC_ERROR}: {exc}")
        raise 


api = Api()