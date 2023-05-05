import random
import string

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request

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

stand_by_player = []


@app_fastapi.get("/api/start")
async def index(request: Request):
    player_id = request.body()
    stand_by_player.append(player_id)
    # room_id = ''.join(random.choices(string.ascii_letters + string.igits, k=10))

    def join_room(players):
        # 長さ10のランダムなアルファベットと数字の組み合わせを生成する
        room_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        print(room_id)
        for player in players:
            # sio.enter_room(sid=player[1], room=room_id)

            # sio.emit("room-full", room=room_id)

    if len(stand_by_player) >= 5:
        join_room(stand_by_player[0:5])
        del stand_by_player[0:5]
    return None
    return room_id
