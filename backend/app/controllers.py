import string
import random
from datetime import datetime

import eventlet
import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.websockets import WebSocket

# class MyCustomNamespace(socketio.AsyncNamespace):  # 名前空間を設定するクラス

#     def on_connect(self, sid, environ):
#         print('[{}] connet sid : {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), sid))
#         print('[{}] connet env : {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), environ))

#     def on_sid_message(self, sid, msg):  # 送信してきたクライアントだけにメッセージを送る関数
#         self.emit('response', msg, room=sid)
#         print('[{}] emit sid : {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), msg))

#     def on_skip_sid_message(self, sid, msg):  # 送信してきたクライアントを除く全ての接続しているクライアントにメッセージを送信する関数
#         self.emit('response', msg, skip_sid=sid)
#         print('[{}] emit skip sid : {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), msg))

#     def on_broadcast_message(self, sid, msg):  # 接続しているすべてのクライアントにメッセージを送る関数
#         self.emit('response', msg)
#         print('[{}] emit all : {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), msg))

#     def on_disconnect(self, sid):
#         print('[{}] disconnect'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


# setup fastapi
app_fastapi = FastAPI()
sio = socketio.AsyncServer(async_mode='asgi')
# sio.register_namespace(MyCustomNamespace('/socket.io'))  # 名前空間を設定
app_socketio = socketio.ASGIApp(sio, other_asgi_app=app_fastapi)  # wsgiサーバーミドルウェア生成
# eventlet.wsgi.server(eventlet.listen(('localhost', 3000)), app_asgi)  # wsgiサーバー起動


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


@app_fastapi.get("/")
async def index(request: Request):
    return views.TemplateResponse('sample.html', {'request': request})


@app_fastapi.post("/api/input_word")
async def input_word(request: Request):

    return None


@app_fastapi.get("/ping/{sid}")
async def ping(sid: str):
    """指定されたsidにemitするエンドポイント
    """
    sio.start_background_task(
        sio.emit,
        "ping", {"message": "ping from server"}, room=sid)
    return {"result": "OK"}


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


standByPlayer = []


@sio.on("AutoMatchingPreLogin")
async def auto_matching_pre_login(playerId):
    standByPlayer.append(playerId)
    print("現在の待機プレイヤー：" + len(standByPlayer) + "名")

    def joinRoom(player1, player2, player3, player4):
        # 長さ10のランダムなアルファベットと数字の組み合わせを生成する
        room_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        print(room_id)
        sio.emit("FullRoom", room_id)


io.sockets.on("connection", function(socket) {
  console.log("connected");
  // オートマッチング機能
  socket.on("AutoMatchingPreLogin", function(playerId) {
    standByPlayer.push(playerId);
    console.log("現在の待機プレイヤー：" + standByPlayer.length + "名");
    function joinRoom(player1, player2) {
      let roomId=Math.random().toString(32).substring(2);
      io.emit("FullRoom", roomId, player1, player2); }
    if (standByPlayer.length >= 2) {
      let player1=standByPlayer[0];
      let player2=standByPlayer[1];
      standByPlayer.splice(0, 2);
      setTimeout(function() {
        joinRoom(player1, player2); }, 1000);     }
  });
