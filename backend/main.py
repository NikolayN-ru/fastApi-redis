import aioredis
import asyncio
from fastapi import Body, FastAPI
from typing import List, Optional
import datetime
import redis

now = datetime.datetime.now()
app = FastAPI()

@app.post("/visited_links")
async def update_item(*, links: List[str] = Body(..., embed=True)):
    results = {"links": links}
    linksArray = results["links"]
    array = []
    linksArray = [array.append({"link": i, "time": now.strftime("%Y-%m-%d %H:%M:%S")}) for i in linksArray]
    print(array)
    return (results)


# class Service:
#     def __init__(self, redis: Redis) -> None:
#         self._redis = redis
#
#     async def process(self) -> str:
#         await self._redis.set("my-key", "value")
#         return await self._redis.get("my-key", encoding="utf-8")


@app.post('/redis')
async def redisTest():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.lpush('myqueue', 'myelement')
    return ('wwwdw')


@app.get('/api/{city}')
async def weather(city: str):
    redis = await aioredis.create_redis(address=('redis', 6379))
    cache = await redis.get(city)
    if cache is not None:
        return {'city': city, 'temperature': cache, 'source': 'cache'}
    await redis.set(city)
    return {'city': city, 'source': 'pogoda.mail.ru'}
