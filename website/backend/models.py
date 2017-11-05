from django.db import models

# Create your models here.

class NKTO_User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 16)
    email = models.CharField(max_length = 32)
    password = models.CharField(max_length = 32)
    phone = models.CharField(max_length = 16)
    icon = models.CharField(max_length=255)
    point = models.IntegerField(default = 0)
    last_login_time = models.DateField(auto_now=True)
    signup_time = models.DateField(auto_now_add = True)
    type = models.IntegerField(default= 0)
    state = models.IntegerField(default = 0)
    def __str__(self):
        return self.name

class NKTO_Goods(models.Model):
    gid = models.AutoField(primary_key=True)
    owner = models.IntegerField(default = 0)
    price = models.FloatField()
    name = models.CharField(max_length = 32)
    answer = models.CharField(max_length = 255)
    eval_price = models.FloatField()
    category = models.IntegerField(default = 0)
    state = models.IntegerField(default = 0)
    def __str__(self):
        return self.name

class NKTO_Purchase(models.Model):
    pid = models.AutoField(primary_key=True)
    uid = models.IntegerField(default = 0)
    gid = models.IntegerField(default = 0)
    state = models.IntegerField(default = 0)
    tran_time = models.DateField()
    tran_place = models.CharField(max_length = 255)
    last_time = models.DateField(auto_now=True)
    def __str__(self):
        return self.pid

class NKTO_Collect(models.Model):
    collid = models.AutoField(primary_key=True)
    uid = models.IntegerField(default = 0)
    gid = models.IntegerField(default = 0)
    def __str__(self):
        return self.collid

class NKTO_ViewLog(models.Model):
    vid = models.AutoField(primary_key=True)
    uid = models.IntegerField(default=0)
    gid = models.IntegerField(default=0)
    view_time = models.DateField(auto_now=True)
    def __str__(self):
        return self.vid

class NKTO_Category(models.Model):
    cateid = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 32)
    def __str__(self):
        return self.cateid

class NKTO_Session(models.Model):
    sid = models.AutoField(primary_key=True)
    uid = models.IntegerField(default=0)
    ip = models.CharField(max_length=32)
    login_time = models.DateField(auto_now=True)
    error_times = models.IntegerField(default=0)
    def __str__(self):
        return self.sid    
    
class NKTO_Blacklist(models.Model):
    bid = models.AutoField(primary_key=True)
    uid = models.IntegerField(default=0)
    adminid = models.IntegerField(default=0)
    effect_time = models.DateField(auto_now=True)
    over_time = models.DateField()
    def __str__(self):
        return self.bid

class NKTO_GoodsDts(models.Model):
    gdid = models.AutoField(primary_key=True)
    gid = models.IntegerField(default=0)
    pic = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    def __str__(self):
        return self.gdid

class NKTO_Question(models.Model):
    qid = models.AutoField(primary_key=True)
    cateid = models.IntegerField(default=0)
    qbody = models.CharField(max_length=255)
    qweight = models.CharField(max_length=255)
    def __str__(self):
        return self.qid

class NKTO_Anwser(models.Model):
    aid = models.AutoField(primary_key=True)
    qid = models.IntegerField(default=0)
    abody = models.CharField(max_length=255)
    aweight = models.IntegerField(default=0)
    def __str__(self):
        return self.aid
    
    
    
    
    