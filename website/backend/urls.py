from django.conf.urls import url
from django.contrib import admin
from .apis import user, goods

urlpatterns = [
	#apis
    url(r'^api/user/signup/$', user.user_register),
    url(r'^api/user/signin/$', user.user_login),
    url(r'^api/user/logout/$', user.user_logout),
    url(r'^api/user/validate/$', user.user_validate),
    url(r'^api/user/storeimage/$', user.user_storeimage),
    url(r'^api/goods/newitems/$', goods.new_item)
]