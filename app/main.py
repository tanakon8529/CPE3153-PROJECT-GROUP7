from fastapi import FastAPI, Request, Response
from fastapi_redis_cache import FastApiRedisCache, cache, cache_one_day
from sqlalchemy.orm import Session
from libs.setting import LOCAL_REDIS_URL

import os

app = FastAPI(title="CPE3151-Group7")

@app.on_event("startup")
def startup():
    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url=os.environ.get("REDIS_URL", LOCAL_REDIS_URL),
        prefix="myapi-cache",
        response_header="X-MyAPI-Cache",
        ignore_arg_types=[Request, Response, Session]
    )

@app.get("/")
def index():
    return {"API-CPE3153": "Group7 Welcome"}

@app.get("/save_word/{word}")
@cache_one_day()
def test_save(word: str):
    return { word : "this data should be cached for 24 hours"}

