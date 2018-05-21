from django.shortcuts import render,HttpResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt
import dicttoxml
# Create your views here.

@csrf_exempt
def call_api_page(request):
    if request.method=='GET':
        return render(request,'call_api/index.html')
    else:
        dc = json.loads(request.body.decode('utf-8'))
        fields = dc.get('fields')
        row  = dc.get('row')
        normed_row = {f:row.get(f) for f in fields}
        xml = dicttoxml.dicttoxml(normed_row,custom_root='REQUEST')
        
        try:
            rt = requests.post(dc.get('rq_url'),data=xml)
            if rt.status_code == 200:
                out= rt.content
            else:
                out = 'error code is %s'%rt.status_code
        except requests.exceptions.RequestException as e:
            out = 'Exception : %s'%str(e)
        dc={
            'xml':xml,
            'rt':out.decode('utf-8')
        }
        return HttpResponse(content=json.dumps(dc),content_type="application/json")
        
