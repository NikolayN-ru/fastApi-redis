from fastapi import Body, FastAPI
from typing import List, Optional
import redis
import datetime, time

app = FastAPI()


def linkRename(link):
    return link.split('//')[-1].split('?')[0]


@app.post("/visited_links")
async def update_item(from1: int = 0, to: int = 0, links: List[str] = Body(..., embed=True)):
    print(from1, to, 'query - question')
    redis_client = redis.Redis(host='docker.for.mac.localhost', port=6379, db=0)
    sec = time.time()
    if redis_client.get('links'):
        oldLinks = redis_client.get('links')
        newLinks = str(oldLinks)
        arr = []
        oldTime = []
        for i in range(len(newLinks.split('link'))):
            arr.append(newLinks.split('link')[i].split(',')[0][6:-2])
            oldTime.append(newLinks.split('time')[i].split(',')[0].split('}')[0][4:])
        print(oldTime[1:])
        print(arr[1:])
        results = {"links": links}
        linksArray = results["links"]
        for i in linksArray:
            if linkRename(i) in arr:
                pass
            else:
                arr.append(i)
                oldTime.append(round(sec))
        redis_client = redis.Redis(host='docker.for.mac.localhost', port=6379, db=0)
        lastArr = []
        for i in range(len(arr)):
            print(i)
            lastArr.append({"link": arr[i], "time": oldTime[i]})
        print('lastArr', lastArr)
        redis_client.set('links', lastArr), 'set'
        return arr[1:]
    else:
        results = {"links": links}
        linksArray = results["links"]
        array = []
        [array.append({"link": linkRename(i), "time": round(sec)}) for i in linksArray]
        newArr = []
        for i in array:
            newArr.append(str(i))
        liksStr = (str(newArr))
        redis_client = redis.Redis(host='docker.for.mac.localhost', port=6379, db=0)
        redis_client.set('links', liksStr), 'set'
        return array


@app.get('/visited_domains')
def redisTest():
    redis_client = redis.Redis(host='docker.for.mac.localhost', port=6379, db=0)
    if redis_client.get('links'):
        oldLinks = redis_client.get('links')
        newLinks = str(oldLinks)
        arr = []
        for i in range(len(newLinks.split('link'))):
            arr.append(newLinks.split('link')[i].split(',')[0][6:-2])
        return arr[1:]
    newArr = []
    return newArr
