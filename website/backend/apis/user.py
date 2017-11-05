import json,hashlib,re, datetime
from .. import models
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.http import HttpResponse, JsonResponse

def generate_md5(s):
    '''返回哈希后的结果'''
    md5 = hashlib.md5()
    md5.update(s.encode('utf8'))
    return md5.hexdigest()

@ensure_csrf_cookie
def user_register(request):
    print('fuck')
    if hasattr(request, 'body'):
        info = json.loads(request.body.decode('utf8'))
        #先检查是不是已经存在
        res = models.NKTO_User.objects.get(email = info['email'])
        if len(res) > 0:
            return JsonResponse({'flag': -2, 'msg': "already exist"})

        password = generate_md5(info['password'])
        time =  datetime.datetime.now()
        #这里应该发送一封邮件
        models.NKTO_User.objects.create(name = info['username'], email = info['email'], password = password,
            phone = info['phonenumber'], icon="https://pbs.twimg.com/profile_images/618435565159997441/Dn7G6RLB_400x400.jpg",
            point = 0, last_login_time = time, signup_time = time, type = 1, state = 0)
        return JsonResponse({'flag': 100, 'msg': 'signup sucess'})
    else:
        return JsonResponse({'flag': -1, 'msg': 'signup failure'})

@ensure_csrf_cookie
def user_login(request):
    if hasattr(request, 'body'):
        info = json.loads(request.body.decode('utf8'))
        check = re.match(r'1[3458]\d{9}', info['username'])
        if check != None:
            obj = models.NKTO_User.objects.filter(phone = info['username'])
            if len(obj) > 0:
                password = generate_md5(info['password'])
                if password == obj[0].password:
                    #更新时间
                    request.session['uid'] = obj[0].uid
                    request.session['type'] = obj[0].type
                    print(request.session['uid'])
                    print(request.session['type'])
                    return JsonResponse({'flag': 1, 'msg': 'login success'})
                else:
                    return JsonResponse({'flag': -1, 'msg': 'wrong password'})
            else:
                return JsonResponse({'flag': -2, 'msg': 'no such account'})
        else:
            obj = models.NKTO_User.objects.filter(email = info['username'])
            if len(obj) > 0:
                password = generate_md5(info['password'])
                if password == obj[0].password:
                    #更新时间
                    obj[0].save()
                    request.session['uid'] = obj[0].uid
                    request.session['type'] = obj[0].type
                    print(request.session['uid'])
                    print(request.session['type'])
                    return JsonResponse({'flag': 1, 'msg': 'login success'})
                else:
                    return JsonResponse({'flag': -1, 'msg': 'wrong password'})
            else:
                return JsonResponse({'flag': -2, 'msg': 'no such account'})
    else:
        return JsonResponse({'flag': -3, 'msg': 'fail to log in'})

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
            pass
    else:
        pass