import random
import string
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
# sio = socketio.Server(cors_allowed_origins='*')
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
# sio.register_namespace(MyCustomNamespace('/socket.io'))  # 名前空間を設定
app_socketio = socketio.ASGIApp(sio, other_asgi_app=app_fastapi)  # wsgiサーバーミドルウェア生成
# app_socketio = socketio.WSGIApp(sio)  # wsgiサーバーミドルウェア生成
eventlet.wsgi.server(eventlet.listen(('localhost', 3000)), app_socketio)  # wsgiサーバー起動


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


@app_fastapi.get("/matchwaiting")
async def match_wating(request: Request):
    return views.TemplateResponse('sample.html')


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


stand_by_player = []


@sio.event
async def start(sid):
    print("hoge")
    # stand_by_player.append([player_id, sid])
    # print("現在の待機プレイヤー：" + len(stand_by_player) + "名")

    # def join_room(players):
    #     # 長さ10のランダムなアルファベットと数字の組み合わせを生成する
    #     room_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    #     print(room_id)
    #     for player in players:
    #         sio.enter_room(sid=player[1], room=room_id)

    #     sio.emit("room-full", room=room_id)

    # if len(stand_by_player) >= 5:
    #     join_room(stand_by_player[0:5])
    #     del stand_by_player[0:5]
    return None


@sio.event
async def connect(sid, environ):
    """socketioのconnectイベント
    """
    print('connect ', sid)

    # standByPlayer = []

    # @sio.on("AutoMatchingPreLogin")
    # async def auto_matching_pre_login(player_id):
    #     standByPlayer.append(player_id)
    #     print("現在の待機プレイヤー：" + len(standByPlayer) + "名")

    #     def joinRoom(player1, player2, player3, player4, player5):
    #         # 長さ10のランダムなアルファベットと数字の組み合わせを生成する
    #         room_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    #         print(room_id)
    #         sio.emit("FullRoom", room_id)
    #         if len(standByPlayer) >= 5:
    #             player1 = standByPlayer[0]
    #             player2 = standByPlayer[1]
    #             player3 = standByPlayer[2]
    #             player4 = standByPlayer[3]
    #             player5 = standByPlayer[4]
    #             del standByPlayer[0:5]
    #             joinRoom(player1, player2, player3, player4, player5)

    # @sio.on("LeaveWaitingRoom")
    # async def leave_waiting_room(player_id):
    #     idx = standByPlayer.index(player_id)
    #     del standByPlayer[idx]
    #     print("現在の待機プレイヤー：" + len(standByPlayer) + "名")
    #     print(standByPlayer)

    # num_clients = {}
    # # num_player = {}

    # @sio.on("login")
    # async def login(room_id):
    #     if not room_id in num_clients:
    #         num_clients[room_id] = 1
    #     else:
    #         num_clients[room_id] += 1

    #     if num_clients[room_id] > 5:
    #         print("This room is full.")
    #     else:
    #         sio.enter_room(room=room_id)
    #         print("roomに入室が完了しました")
    #         print(room_id)
    #         print("今のroomにいる人数"+num_clients[room_id])


@sio.event
async def disconnect(sid):
    """socketioのdisconnectイベント
    """
    print('disconnect ', sid)
