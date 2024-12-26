import redis
from src.configs.env import get_settings
from typing import Optional

config = get_settings()

class RedisCache:
  def __init__(self):
    self.redis_cache: Optional[redis] = None
    
  async def init_cache(self):
    self.redis_cache = redis.from_url(
      f"redis://{config.redis_host}:{config.redis_port}/{config.redis_db}?encoding=utf-8&decode_responses=True"
    )
  
  async def keys(self, pattern):
    """
    Returns all keys with a specified pattern (similar but simplier form of regex)
    """
    return self.redis_cache.keys(pattern)
  
  async def set(self, key, value, expiration_time_in_seconds):
    return self.redis_cache.set(key, value, ex=expiration_time_in_seconds)
  
  async def get(self, key):
    return self.redis_cache.get(key)
  
  async def delete(self, key):
    return self.redis_cache.delete(key)
  
  async def delete_all(self, keys):
    return self.redis_cache.delete(*keys)
  
  async def close(self):
    self.redis_cache.close()
    
  async def ping(self):
    return self.redis_cache.ping()
  
  def __add__(self, b):
    return self.salary + b.salary
  
redis_cache = RedisCache()