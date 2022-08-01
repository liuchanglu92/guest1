#Django模型文件，创建应用程序数据表模型（对应数据库的相关操作）
from django.db import models
# 发布会表
class Event(models.Model):
    name = models.CharField(max_length=100) #发布会标题
    limit=models.IntegerField()  #参会人数
    status=models.BooleanField() #状态
    address=models.CharField(max_length=200) #发布会地址
    start_time=models.DateTimeField('enents time') #发布会开始时间
    create_time=models.DateTimeField(auto_now=True)  #创建时间（自动获取当前时间）

    def __str__(self):
        return  self.name
#嘉宾表
class Guest(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE) #on_deletet 删除关联数据，与之也删除
    realname=models.CharField(max_length=64)
    phone=models.CharField(max_length=16)
    email=models.EmailField()
    sign=models.BooleanField()
    create_time=models.DateTimeField(auto_now=True)

    class Mate:
        unique_together=("enent","phone")

    def _self_(self):
        return self.realname