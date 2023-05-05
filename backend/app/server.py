import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins='*')
app_socketio = socketio.WSGIApp(sio)  # wsgiサーバーミドルウェア生成


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


@sio.event
async def join_room(sid):
    sio.enter_room(sid=sid)
    print(sid, " joined room ", room)


@sio.event
async def leave_room(sid, room):
    sio.leave_room(sid=sid, room=room)
    print(sid, " left room ", room)


@sio.event
async def send_message(sid, message, room):
    await sio.emit('message', message, room=room)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('localhost', 3000)), app_socketio)  # wsgiサーバー起動
