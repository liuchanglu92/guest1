# 添加发布会接口
from django.http import JsonResponse
from sign.models import Event
from django.core.exceptions import ValidationError , ObjectDoesNotExist

def add_event(request):
    eid = request.POST.get('eid', '')
    name = request.POST.get('name', '')
    limit = request.POST.get('limit', '')
    status = request.POST.get('status', '')
    address = request.POST.get('address', '')
    start_time = request.POST.get('start_time', '')

    if eid == '' or name == '' or limit == '' or address == '' or start_time == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})

    result = Event.objects.filter(id=eid)
    if result:
        return JsonResponse({'status': 10022, 'message': 'event id is already exiets'})

    result = Event.objects.filter(name=name)
    if result:
        return JsonResponse({'status': 10023, 'message': 'event name is already exieis'})
    if status == '':
        status = 1

    try:
        Event.objects.create(id=eid, name=name, limit=limit, status=int(status), address=address, start_time=start_time)
    except ValidationError as e:
        error = 'strat_time format error'
        return JsonResponse({'status': 10024, 'message': 'error'})
    return JsonResponse({'status': 200, 'message': 'success'})

def get_event_list(request):
    eid = request.Get.get("eid","")
    name = request.Get.get("name","")

    if eid == '' and name == ' ':
        return  JsonResponse({'status':10021,'message':'parameter error'})

    if eid !='':
        event={}
        try:
            result = Event.objects.get(id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':10022,'message':'query result is emtpy'})
        else:
            event['name']=result.name
            event['limit']=result.limit
            event['status']=result.status
            event['address'] = result.address
            event['start_time'] = result.start_time
            event['create_time'] = result.create_time
            return  JsonResponse({'status':200,'message':'success','data':event})

    if name !='':
        datas = []
        results = Event.objects.filter(name__contains=name)
        if results:
            for r in results:
                event = {}
                event['name'] = r.name
                event['limit'] = r.limit
                event['status'] = r.status
                event['address'] = r.address
                event['start_time'] = r.start_time
                datas.append(event)
            return JsonResponse({'status':200,'message':'success','data':datas})
        else:
            return  JsonResponse({'status':10022,'message':'query result is empty'})# 添加发布会接口


def add_event(request):
    eid = request.POST.get('eid', '')
    name = request.POST.get('name', '')
    limit = request.POST.get('limit', '')
    status = request.POST.get('status', '')
    address = request.POST.get('address', '')
    start_time = request.POST.get('start_time', '')

    if eid == '' or name == '' or limit == '' or address == '' or start_time == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})

    result = Event.objects.filter(id=eid)
    if result:
        return JsonResponse({'status': 10022, 'message': 'event id is already exiets'})

    result = Event.objects.filter(name=name)
    if result:
        return JsonResponse({'status': 10023, 'message': 'event name is already exieis'})
    if status == '':
        status = 1

    try:
        Event.objects.create(id=eid, name=name, limit=limit, status=int(status), address=address, start_time=start_time)
    except ValidationError as e:
        error = 'strat_time format error'
        return JsonResponse({'status': 10024, 'message': 'error'})
    return JsonResponse({'status': 200, 'message': 'success'})

def get_event_list(request):
    eid = request.Get.get("eid","")
    name = request.Get.get("name","")

    if eid == '' and name == ' ':
        return  JsonResponse({'status':10021,'message':'parameter error'})

    if eid !='':
        event={}
        try:
            result = Event.objects.get(id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':10022,'message':'query result is emtpy'})
        else:
            event['name']=result.name
            event['limit']=result.limit
            event['status']=result.status
            event['address'] = result.address
            event['start_time'] = result.start_time
            event['create_time'] = result.create_time
            return  JsonResponse({'status':200,'message':'success','data':event})

    if name !='':
        datas = []
        results = Event.objects.filter(name__contains=name)
        if results:
            for r in results:
                event = {}
                event['name'] = r.name
                event['limit'] = r.limit
                event['status'] = r.status
                event['address'] = r.address
                event['start_time'] = r.start_time
                datas.append(event)
            return JsonResponse({'status':200,'message':'success','data':datas})
        else:
            return  JsonResponse({'status':10022,'message':'query result is empty'})