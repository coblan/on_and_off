from django.conf import settings
import requests
import json

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
            data={
                'fun':'get_query',
                #'start': self.start,
                #'end': self.end,
                'model': 'TTaskinfo',
                'page':page, 
                'perpage':perpage, 
                'filters': {
                    'discovertime__gte': self.start,
                    'discovertime__lte': self.end,
                    'enterpriseinvoled': 1,
                    #'streetcode': 1806
                  
                    },
            }
            rt = requests.post(url,data=json.dumps(data), proxies = proxies)
            case_list = json.loads(rt.text)
            for item in case_list:
                yield item
            
            if len(case_list) < perpage:
                has_next = False
            else:
                page += 1
