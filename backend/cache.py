import aioredis
import json
from functools import wraps

redis_client = aioredis.from_url("redis://localhost")

async def get_cache(key: str):
    value = await redis_client.get(key)
    if value:
        return json.loads(value)
    return None

async def set_cache(key: str, value: any, ttl: int = 300):
    await redis_client.set(key, json.dumps(value), ex=ttl)

async def delete_cache(key: str):
    await redis_client.delete(key)

async def invalidate_cache(pattern: str):
    keys = await redis_client.keys(pattern)
    if keys:
        await redis_client.delete(*keys)

# Decorator for caching function results

def cache_with_ttl(ttl: int):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}:{args}:{kwargs}"
            cached_result = await get_cache(cache_key)
            if cached_result is not None:
                return cached_result
            result = await func(*args, **kwargs)
            await set_cache(cache_key, result, ttl=ttl)
            return result
        return wrapper
    return decorator