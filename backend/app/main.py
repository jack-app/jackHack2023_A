import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from router import app_fastapi
from starlette.websockets import WebSocket

# # setup fastapi
# app_fastapi = FastAPI()

# origins = [
#     "http://localhost:3000",
# ]

# app_fastapi.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# setup socketio
sio = socketio.AsyncServer(async_mode='asgi')
app_socketio = socketio.ASGIApp(sio, other_asgi_app=app_fastapi)


# @app_fastapi.get("/")
# async def index():
#     """fastapiのAPI実装(socketioに関係ない)
#     """
#     return {"result": "Index"}


# @app_fastapi.get("/ping/{sid}")
# async def ping(sid: str):
#     """指定されたsidにemitするエンドポイント
#     """
#     sio.start_background_task(
#         sio.emit,
#         "ping", {"message": "ping from server"}, room=sid)
#     return {"result": "OK"}


@sio.event
async def connect(sid, environ):
    """socketioのconnectイベント
    """
    print('connect ', sid)


@sio.event
async def disconnect(sid):
    """socketioのdisconnectイベント
    """
    print('disconnect ', sid)
