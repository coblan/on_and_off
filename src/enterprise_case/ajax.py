from django.conf import settings
import requests
import json
import dicttoxml
import xmltodict

proxies = getattr(settings,'DATA_PROXY',{})

def get_global():
    return globals()

def info_enterprise(name): 
    dc = {
        'USER_NAME': 'wangge',
        'PASSWD': '96e79218965eb72c92a549dd5a330112',
        'ENTY_TYPE': '02',
        'ENTY_NAME': name,
    }
    #dc = json.loads(request.body.decode('utf-8'))
    #fields = dc.get('fields')
    #row  = dc.get('row')
    #normed_row = {f:row.get(f) for f in fields}
    normed_row = dc
    xml = dicttoxml.dicttoxml(normed_row,custom_root='REQUEST',attr_type = False)

    try:
        rt = requests.post(settings.INFO_SERVICE,data= {'info': xml,}, proxies = proxies)
        if rt.status_code == 200:
            out= rt.text
            rt_dc = xmltodict.parse(out)
        else:
            out = 'error code is %s'%rt.status_code
    except requests.exceptions.RequestException as e:
        out = 'Exception : %s'%str(e)
    
    bb = rt_dc['RESPONSE']['EntyBasicInfo']
    if not isinstance(bb, list):
        out_list = [bb]
    else:
        out_list = bb
    
    
    return out_list

    
