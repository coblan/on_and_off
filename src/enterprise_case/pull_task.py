from .port.sangao_bridge import JianduPort
from enterprise_case.models import TTaskinfo
from django.utils.timezone import datetime, timedelta
import time
import json

import logging
log = logging.getLogger('manage_task')

def pull_task(start = None, end = None): 
    log.info('-' * 30)
    log.info('开始抓取【监督员】按键')
    
    today_str = datetime.now().strftime('%Y-%m-%d %H:%M:%D')

    print('start fetch jiandu %s' % today_str)
    
    tomorro = datetime.now() + timedelta(days = 1)
    tomorro_str = tomorro.strftime('%Y-%m-%d')
    
    if not start:
        lastone = TTaskinfo.objects.order_by('-discovertime').first()
        if lastone:
            start = str(lastone.discovertime)[:10]
        else:
            start = today_str[:10]
    if not end:
        end= tomorro_str

    
    log.info('开始时间%s ; 结束时间%s' % (start, end))
    spd =  JianduPort(start = start, end = end)

    ls = []
    count = 0
    created_count = 0
    for row in spd.get_data():
        count += 1

        #loc_x,loc_y = cord2loc(float( row.get('coordx') ),float( row.get('coordy') ))
        
        #keeper = row['keepersn'] if  row['keepersn'] else None
        def_data = dict(row)
        def_data.pop('taskid')
             
        log.info(row['taskid'])
        obj, created = TTaskinfo.objects.update_or_create(taskid = row['taskid'], defaults = def_data)
        if created:
            created_count += 1

    log.info('监督员按键抓取完成，总共抓取了 %s ,新建了 %s ' % (count, created_count) )
    return created_count
