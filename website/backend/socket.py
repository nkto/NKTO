from django.shortcuts import render
import socketio
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt
import hashlib, time, datetime
import urllib.parse

async_mode = None
sio = socketio.Server(async_mode = async_mode)
slist = [1]*2
thread = None
"""
talker_list以cid或uid为key存储sid customer_list以cid为key存储uid列表 conversation以uid为key存储聊天内容
"""

@csrf_exempt
def model(request):
    return render(request, 'nktoindex.html')

def time2str():
    date = datetime.datetime.now()
    return date.strftime('%Y-%m-%d %H:%M:%S')

def str2time(st):
    t = time.strptime(st, '%Y-%m-%d %H:%M:%S')
    return time.mktime(t)

@sio.on('sendmessage', namespace = '/test')
def send_message(sid, message):
    uid = 1 - int(message['uid'])
    sio.emit('getresponse', {'data': message['data'], 'time': message['time'], 'src': message['src']}, room = slist[uid], namespace = '/test')


@sio.on('connected', namespace = '/test')
def connected(sid, message):
    uid = int(message['uid'])
    print(uid)
    slist[uid] = sid

@sio.on('disconnect request', namespace = '/test')
def disconnect_request(sid):
    sio.disconnect(sid, namespace = '/test')

@sio.on('disconnect', namespace = '/test')
def test_disconnect(sid):
    print('Client disconnected')