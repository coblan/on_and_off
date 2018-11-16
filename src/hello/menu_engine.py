# encoding:utf-8

from __future__ import unicode_literals

from helpers.director.shortcut import page_dc
from helpers.director.engine import BaseEngine,page,fa
from django.contrib.auth.models import User, Group
from helpers.director.engine import BaseEngine, page, fa, can_list, can_touch
from helpers.maintenance.update_static_timestamp import js_stamp
from . import permit
from enterprise_case.models import Enterprise, TTaskinfo

class PcMenu(BaseEngine):
    url_name='EnterpriseCase'
    brand='事中事后'
    mini_brand='系统'
    
    @property
    def menu(self): 
        crt_user = self.request.user
        menu=[
            #{'label':'主页','url':page('home'),'icon':fa('fa-home'), }, 
            {'label':'案件管理','icon':fa('fa-user-secret'),
             'submenu':[
                 {'label':'案件列表','url':page('enterprise_case.caseadmin'), 'visible': can_touch(TTaskinfo, crt_user), },
                 #{'label':'案件走势','url':page('inspector.inspector')},
    
                 ]},
             {'label':'重点监管','icon':fa('fa-user-secret'), 
              'submenu':[
                 {'label':'企业监管','url':page('Enterprise.table'), 'visible': can_touch(Enterprise, crt_user),},
                 ]},
             {'label': '系统管理', 'icon': fa('fa-user'), 'visible': True,
              'submenu': [
                  {'label':'用户', 'url': page('jb_user'), 'visible': can_touch(User, crt_user)},
                  {'label': '权限组', 'url': page('jb_group'), 'visible': can_touch(Group, crt_user)},
                 ]},
        ]
        return menu
    
    def custome_ctx(self, ctx):
        ctx['js_stamp']=js_stamp
        ctx['fast_config_panel']=True
        ctx['menu_expand_all'] = True

        return ctx        
 

PcMenu.add_pages(page_dc)


class ProgramerMenu(BaseEngine):
    url_name='Programer'
    brand='Programer'
    mini_brand='Programer'
    menu=[
        
        #{'label':'GIS区域','url':page('geoinfo.blockpolygon'),'icon':fa('fa-map-o')},
        {'label':'区域编辑','url':page('geoscope.blockgroup'),'icon':fa('fa-map-o')},
 
        {'label':'参数设置','url':page('kv'),'icon':fa('fa-map-o')},
        
        
    ]  
    
    def custome_ctx(self, ctx):
        ctx['js_stamp']=js_stamp
        if not 'table_fun_config' in ctx:
            ctx['table_fun_config'] ={
                'detail_link': '详情', #'<i class="fa fa-info-circle" aria-hidden="true" title="查看详情"></i>'#,
            }
        return ctx 

ProgramerMenu.add_pages(page_dc)
