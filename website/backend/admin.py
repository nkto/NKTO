from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(NKTO_User)
admin.site.register(NKTO_Goods)
admin.site.register(NKTO_Purchase)
admin.site.register(NKTO_Collect)
admin.site.register(NKTO_ViewLog)
admin.site.register(NKTO_Category)
admin.site.register(NKTO_Session)
admin.site.register(NKTO_Blacklist)
admin.site.register(NKTO_GoodsDts)
admin.site.register(NKTO_Question)
admin.site.register(NKTO_Anwser)