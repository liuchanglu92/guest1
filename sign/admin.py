#映射models中的数据到Django自带的admin后台\
from django.contrib import admin
from sign.models import Event,Guest

class EventAdmin(admin.ModelAdmin):
    list_display = ['id','name','status','address','start_time'] #后台管理显示字段
    search_fields = ['name']  #根据name搜索
    list_filter = ['status']  #过滤器

class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname','phone','email','sign','create_time','event']
    search_fields = ['realname','phone']
    list_filter = ['sign']
admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)