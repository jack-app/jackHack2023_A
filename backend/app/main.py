import socketio
# from router import app_fastapi
from controllers import app_socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.websockets import WebSocket

# # setup socketio
# sio = socketio.AsyncServer(async_mode='asgi')
# app_socketio = socketio.ASGIApp(sio, other_asgi_app=app_fastapi)


# @sio.event
# async def connect(sid, environ):
#     """socketioのconnectイベント
#     """
#     print('connect ', sid)


# @sio.event
# async def disconnect(sid):
#     """socketioのdisconnectイベント
#     """
#     print('disconnect ', sid)


# @sio.event
# async def join_room(sid, room):
#     sio.enter_room(sid=sid, room=room)
#     print(sid, " joined room ", room)


# @sio.event
# async def leave_room(sid, room):
#     sio.leave_room(sid=sid, room=room)
#     print(sid, " left room ", room)


# @sio.event
# async def send_message(sid, message, room):
#     await sio.emit('message', message, room=room)

# app_fastapi.mount("/socket.io", socketio.WSGIApp(sio))
