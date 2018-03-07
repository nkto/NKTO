from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.http import HttpResponse, JsonResponse
import json,hashlib,re, datetime, time
from .. import models

@ensure_csrf_cookie
def new_item(request):
    obj = models.NKTO_Goods.objects.order_by("time")[0:4]
    items = []
    for i in obj:
        o = models.NKTO_GoodsDts.objects.filter(gid = i.gid, order = 1) #表示查找第一张图片
        item = {}
        item['src'] = o[0].pic
        item['name'] = i.name
        item['value'] = i.price
        items.append(item)
    return JsonResponse({'message': items})

@ensure_csrf_cookie
def generate(request):
    info = json.loads(request.body.decode('utf8'))
    form = info['formitem']
    special = info['special']
    return JsonResponse({'price': form['price']})