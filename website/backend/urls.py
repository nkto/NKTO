from django.conf.urls import url
from django.contrib import admin
from .apis import user, goods
from . import socket

urlpatterns = [
	#apis
    url(r'^api/user/signup/$', user.user_register),
    url(r'^api/user/signin/$', user.user_login),
    url(r'^api/user/logout/$', user.user_logout),
    url(r'^api/user/validate/$', user.user_validate),
    url(r'^api/user/storeimage/$', user.user_storeimage),
    url(r'^api/goods/newitems/$', goods.new_item),
    url(r'^api/user/checkstate/$', user.user_checkstate),
    url(r'^api/goods/generate/$', goods.generate),
    url(r'^socket.io/', socket.model),
]