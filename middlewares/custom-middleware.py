from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import time

app = FastAPI()

class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        print(f"Request: {request.url.path} processed in {round(duration, 2)} seconds")
        return response

app.add_middleware(TimerMiddleware)

@app.get('/hello')
async def hello():
    for i in range(10000000):
        pass
    return {'message': 'hello fastapi'}