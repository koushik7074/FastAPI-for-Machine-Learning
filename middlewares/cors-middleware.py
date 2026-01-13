from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'https://myfrontend.com', 'https://localhost:3000'
    ],
    allow_credentials = True,
    allow_methods = ['GET', 'POSt', 'PUT', 'DELETE'],
    allow_headers = ['*']
)
