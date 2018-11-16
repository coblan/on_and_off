from django.contrib import admin
from helpers.director.shortcut import TablePage, ModelTable, page_dc, director, ModelFields, RowSearch, SimTable, RowFilter, SelectSearch
from .models import TTaskinfo, Enterprise
from helpers.maintenance.update_static_timestamp import js_stamp_dc
from .port.enterpris_info import enterprise_list
from . import admin_enterprise
from .pull_task import pull_task
from . import permit
from helpers.director.access.permit import user_permit_names
import re
# Register your models here.

class CasePage(TablePage):
    template = 'jb_admin/table.html'
    extra_js = ['/static/js/enterprise_case.pack.js?t=%s'%js_stamp_dc.get('enterprise_case_pack_js','')]
    def get_label(self): 
        return '案件列表'
    
    class tableCls(ModelTable):
        pop_edit_field = 'taskid'
        model = TTaskinfo
        exclude = []
        fields_sort = ['taskid', 'deptname', 'address', 'description', 'enterpriseinvoledname', 'ENT_NAME', 'discovertime']
        
        #def inn_filter(self, query): 
            #return query.select_related('enterprise')
        def inn_filter(self, query): 
            if self.crt_user.is_superuser:
                return query
            else:
                permit_names = user_permit_names(self.crt_user)
                code_list = []
                for name in permit_names:
                    mt = re.search('^street\.(\d+)\.case$', name)
                    if mt:
                        code_list.append(mt.group(1))
                return query.filter(streetcode__in = code_list)
        
        
        def getExtraHead(self): 
            return [
                {'name': 'ENT_NAME','label': '企业名称',}
            ]
        
        def dict_head(self, head): 
            dc = {
                'taskid': 150,
                'deptname': 140,
                'address': 160,
                'enterpriseinvoledname': 160,
                'description': 200,
                'ENT_NAME': 160,
                'discovertime': 130,
               
            }
            if dc.get(head['name']):
                head['width'] = dc.get(head['name'])

            return head
        
        def dict_row(self, inst): 
            if inst.enterprise:
                dc =  {
                    'ENT_NAME': inst.enterprise.ENT_NAME, 
                    'DOM': inst.enterprise.DOM,
                    'REG_NO': inst.enterprise.REG_NO,
                    'UNI_SCID': inst.enterprise.UNI_SCID, 
                    'NEIGHBOR': inst.enterprise.NEIGHBOR,
                }
            else:
                dc = {}
            return dc
        
        def get_operation(self): 
            return [
                {'fun': 'director_call',
                 'director_name': 'update_case_from_sangao',
                 'confirm_msg': '确认马上从网格化更新案件吗?',
                 'label': '从网格化更新案件',
                 'after_call': 'refresh',
                 'editor': 'com-op-btn',}, 
            ]
        
        @staticmethod
        def update_case_from_sangao(): 
            count = pull_task()
            return {
                'msg': '成功新建%s条案件!' % count,
            }
        
        class search(RowSearch):
            names = ['taskid', 'enterpriseinvoledname']
            
        
        class filters(RowFilter):
            names = ['deptname']
            def getExtraHead(self): 
                options = [{'value': x.ENT_NAME, 'label': x.ENT_NAME} for x in Enterprise.objects.all() ]
                return [
                    {'name': 'ENT_NAME', 'label': '企业名称','editor': 'com-filter-select','options': options,}
                ]
            
            def clean_query(self, query): 
                if self.kw.get('ENT_NAME'):
                    return query.filter(enterprise__ENT_NAME = self.kw.get('ENT_NAME'))
                else:
                    return query
            
            
            

class CaseForm(ModelFields):
    field_sort = ['taskid', 'enterpriseinvoledname', 'ENT_NAME', 'DOM', 'REG_NO', 'UNI_SCID', 'NEIGHBOR']
    class Meta:
        model = TTaskinfo
        exclude = []
    
    def clean_dict(self, dc): 
        for k in dc:
            if dc[k] == None:
                dc[k] = ''
        return dc
    
    def getExtraHeads(self): 
        return [
            {'name': 'ENT_NAME','label': '企业名称', 'editor': 'linetext','readonly': True,}, 
            {'name': 'DOM','label': '经营地址', 'editor': 'linetext', 'readonly': True,}, 
            {'name': 'REG_NO','label': '企业注册号', 'editor': 'linetext','readonly': True,}, 
            {'name': 'UNI_SCID','label': '统一社会<br>信用代码', 'editor': 'linetext','readonly': True,}, 
            {'name': 'NEIGHBOR','label': '街道', 'editor': 'linetext','readonly': True,}
        ]
    
    def dict_row(self, inst): 
        return {
            'ENT_NAME': inst.enterprise.ENT_NAME,
        }
    
    def dict_head(self, head): 
        if head['name'] =='enterpriseinvoledname':
            head['editor'] = 'com-field-related-query'
            table_obj = CaseSelect(crt_user=self.crt_user)
            #head['editor'] = 'com-field-pop-table-select'
            head['table_ctx'] = table_obj.get_head_context()
            head['options'] = []
        if head['name'] == 'taskid':
            head['editor'] = 'com-field-taskid' 
            head['sango_link'] = 'http://10.231.18.25/CityGridtest/CaseOperate_flat/ParticularDisplayInfo.aspx?taskid={taskid}'
            #head['sango_link'] = 'http://10.231.18.25/CityGrid/caseoperate_flat/Chuli/HuiFuCase.aspx?TaskId={taskid}&categoryId=17A&solvingId=4377107&page=0&returnUrl=TaskInfoList.aspx?categoryId=17A&OpeBtnIds=btn020,btn016,btn019,'
        return head
    
    def save_form(self): 
        kw_dc = {
            'DOM': self.kw.get('DOM'),
            'REG_NO': self.kw.get('REG_NO'),
            'UNI_SCID': self.kw.get('UNI_SCID'),
            'NEIGHBOR': self.kw.get('NEIGHBOR'),
        }
        obj, created = Enterprise.objects.update_or_create(ENT_NAME = self.kw['ENT_NAME'], defaults = kw_dc)
        self.instance.enterprise = obj
        super().save_form()
        

class CaseSelect(SimTable):
    def __init__(self, _page=1, row_sort=[], row_filter={}, row_search='', crt_user=None, perpage=None, **kw): 
        self.enterprise_search_word = row_search
        super().__init__(_page, row_sort, row_filter, row_search, crt_user, perpage, **kw)

    
    #def dict_head(self, head): 
        #if head['name']=='ENT_NAME':
            #head['editor']='com-table-foreign-click-select'
        #return head
    
    def get_head_context(self):
        ctx = super().get_head_context()
        ctx. update({
            'heads': self.get_heads(),
            'row_filters': [self.row_search.get_context()],
            'director_name': self.get_director_name(), 
            'selectable': False,
        })
        return ctx
    
    #def get_data_context(self):
        #ctx = super().get_data_context()
        #rows =  self.get_rows()
        #table_layout = self.getTableLayout(rows)
        #return {
            #'rows': rows,
            #'table_layout': table_layout,
            #'row_pages' : self.getRowPages(), #self.pagenum.get_context(),  
            #'search_args':self.search_args, 
            #'footer': self.footer,
            #'parents': self.getParents(),
        #}
    
        #return {
            #'rows': self.get_rows(),
            #'row_pages' : self.pagenum.get_context(),  
            #'search_args':self.search_args
        #}
    
    def get_heads(self): 
        return [
            {'name': 'ENT_NAME','label': '企业名称','editor':'com-table-foreign-click-select' ,'width': 200,}, 
            {'name': 'DOM','label': '企业地址','width': 250,}, 
            #{'name': 'UNI_SCID','label': '统一社会信用代码',}
        ]
    
    def get_rows(self): 
        if self.enterprise_search_word:
            rows = enterprise_list(self.enterprise_search_word)
        else:
            rows = []
        return rows
    
    class search(RowSearch):
        names = ['enterprise_search_word']
        def get_context(self): 
            dc = {
                'search_tip': '查询关键字',
                'editor':'com-search-filter',
                'name':'_q'
            }
            return dc
        
    

            

director.update({
    'enterprise_case.caseadmin': CasePage.tableCls,
    'enterprise_case.caseadmin.edit': CaseForm,
    'enterprise_case.caseinfo.table.select': CaseSelect, 
    'update_case_from_sangao': CasePage.tableCls.update_case_from_sangao,
})

page_dc.update({
    'enterprise_case.caseadmin': CasePage,
    
})