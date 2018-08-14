from helpers.director.shortcut import TablePage, ModelTable, page_dc, director, RowFilter
from .models import Enterprise
from django.db.models.aggregates import Count,Sum
from django.db.models import F, Q, Case, When

class EnterprisePage(TablePage):
    template = 'jb_admin/table.html'
    def get_label(self): 
        return '企业监管'
    
    class tableCls(ModelTable):
        model = Enterprise
        exclude = []
    
        def getExtraHead(self): 
            return [
                {'name': 'nums_task', 'label': '涉案数目',}, 
                {'name': 'nums_finish_task', 'label': '已结案',}
            ]
        
        def inn_filter(self, query): 
            return query.annotate(nums_task = Count('ttaskinfo'), \
                                  nums_finish_task = Count(Case(When(ttaskinfo__status = 9 , then= 1) )))
        def dict_row(self, inst): 
            return {
                'nums_task': inst.nums_task,
                'nums_finish_task': inst.nums_finish_task,
            }
        
        class filters(RowFilter):
            range_fields = ['ttaskinfo__discovertime']
            def getExtraHead(self): 
                return [
                    {'name': 'ttaskinfo__discovertime', 'editor':'com-date-range-filter','label':'日期',}
                ]
    

director.update({
    'Enterprise.table': EnterprisePage.tableCls,
})

page_dc.update({
    'Enterprise.table': EnterprisePage,
})