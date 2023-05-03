import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.websockets import WebSocket

# setup fastapi
app_fastapi = FastAPI()

origins = [
    "http://localhost:3000",
]

app_fastapi.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

views = Jinja2Templates(directory="views")
jinja_env = views.env  # Jinja2.Environment : filterやglobalの設定用


def index(request: Request):
    return views.TemplateResponse('sample.html', {'request': request})
