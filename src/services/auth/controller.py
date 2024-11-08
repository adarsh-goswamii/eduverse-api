from fastapi import Request
from src.lib.redis import redis_cache
from src.configs.redis_constants import RedisExpInSec, RedisKey

class TestController:
  """Test Controller"""
  
  @classmethod
  async def test(self, request: Request, payload: str):
    try:
      test_data = await redis_cache.get(RedisKey.TEST_DATA)
      
      if test_data == None:
        await redis_cache.set(RedisKey.TEST_DATA, payload, RedisExpInSec.TEST_DATA)
      else:
        return {"message": test_data, "source:": "redis"}
      
      return {"message": "Value set"}
    except Exception as e:
      return {"error": str(e)}
