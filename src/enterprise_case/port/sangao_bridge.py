from django.conf import settings
import requests
import json
from django.db import models
from enterprise_case.models import TTaskinfo
from django.utils.timezone import datetime

proxies = getattr(settings,'DATA_PROXY',{})

class JianduPort(object):
    def __init__(self, start, end): 
        self.start = start
        self.end = end

    def get_data(self):
        url = settings.SANGO_BRIDGE+'/rq'
        has_next = True
        page = 1
        perpage = 300
        
        while has_next:
            #data={
                #'fun':'get_query',
                ##'start': self.start,
                ##'end': self.end,
                #'model': 'TTaskinfo',
                #'page':page, 
                #'perpage':perpage, 
                #'filters': {
                    #'discovertime__gte': self.start ,
                    #'discovertime__lte': self.end , 
                    #'enterpriseinvoled': 1,
                    ##'streetcode': 1806
                  
                    #},
            #}
            data = {
                'fun':'on_and_off_task',
                'start': self.start,
                'end': self.end,
            }
            rt = requests.post(url,data=json.dumps(data), proxies = proxies)
            case_list = json.loads(rt.text)
            fields_names = [x.name for x in TTaskinfo._meta.get_fields()]
            
            for item in case_list:
                small_item = {}
                for k, v in item.items():
                    if k.lower() in fields_names:
                        
                        field = TTaskinfo._meta.get_field(k.lower())
                        if isinstance(field, models.DateTimeField):
                            try:
                                normed_v = datetime.strptime(v, '%Y-%m-%d %H:%M:%S')
                            except:
                                #print('解析时间错误 %s' % v)
                                normed_v = None
                        else:
                            normed_v = v
                        small_item[k.lower()] = normed_v
                yield small_item
            
            if len(case_list) < perpage:
                has_next = False
            else:
                page += 1
