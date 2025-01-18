import os
import redis
from fastapi import FastAPI

app = FastAPI()

redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_password = os.getenv("REDIS_PASSWORD", "")

r = redis.Redis(host=redis_host, port=redis_port, password=redis_password)

@app.get("/")
def read_root():
    visits = r.incr("visits")
    return {"message": f"Hello from FastAPI! This page has been visited {visits} times."}