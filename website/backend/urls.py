from django.conf.urls import url
from django.contrib import admin
from .apis import user



urlpatterns = [
	#apis
    url(r'^api/user/signup/$', user.user_register),
    url(r'^api/user/signin/$', user.user_login),
]