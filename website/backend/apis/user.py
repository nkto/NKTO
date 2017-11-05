import json,hashlib,re
from .. import models
from django.http import HttpResponse, JsonResponse

@ensure_csrf_cookie
def user_register(request):
    if hasattr(request, 'body'):
        info = json.loads(request.body.decode('utf8'))
        password = hashlib.md5(info['password'].encode('utf-8'))
        models.NKTO_User.create(name = info['name'], email = info['email'], password = password,
            phone = info['phone'])
    else:

@ensure_csrf_cookie
def user_login(request):
    if hasattr(request, 'body'):
        info = json.loads(request.body.decode('utf8'))
        check = re.match(r'1[3458]\d{9}', info['username'])
        if check != None:
            obj = models.NKTO_User.filter(phone = info['username'])
            if len(obj > 0):
                password = hashlib.md5(info['password'].encode('utf-8'))
                if password = obj.password:
                    #更新时间
                    obj.update()
                else:
            else:
    else:

@ensure_csrf_cookie
def user_modify(request):
    if hasattr(request, 'body'):
        info = json.loads(request.body.decode('utf8'))
        obj = models.NKTO_User.filter(uid = info['id'])
        if len(obj) > 0:
            if hasattr(info, 'icon'):
                obj.update(icon = info['icon'])
            if hasattr(info, 'name'):
                obj.update(name = info['name'])
            if hasattr(info, 'phone'):
                obj.update(phone = info['phone'])
            if hasattr(info, 'password'):
                password = hashlib.md5(info['password'].encode('utf-8'))
                obj.update(password = password)
        else:
    else: