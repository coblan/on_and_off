from helpers.director.base_data import site_cfg

def get_permit(): 
    permit = [
        { 'label': '街镇案件', 
          'children': [
            {'label': '案件编辑', 'value': 'taskinfo',}, 
            {'label': '夏阳街道', 'value': 'street.1801.case','depend': ['taskinfo']}, 
            {'label': '盈浦街道', 'value': 'street.1802.case','depend': ['taskinfo']}, 
            {'label': '朱家角镇', 'value': 'street.1803.case','depend': ['taskinfo']}, 
            {'label': '练塘镇', 'value': 'street.1804.case','depend': ['taskinfo']},
             {'label': '金泽镇', 'value': 'street.1805.case','depend': ['taskinfo']},
            {'label': '赵巷镇', 'value': 'street.1806.case','depend': ['taskinfo']},
            {'label': '徐泾镇', 'value': 'street.1807.case','depend': ['taskinfo']},
            {'label': '华新镇', 'value': 'street.1808.case','depend': ['taskinfo']}, 
            {'label': '重固镇', 'value': 'street.1809.case','depend': ['taskinfo']}, 
            {'label': '白鹤镇', 'value': 'street.1810.case','depend': ['taskinfo']}, 
            {'label': '香花桥街道', 'value': 'street.1811.case','depend': ['taskinfo']}, 
        ]}, 
         { 'label': '重点监管', 
           'children': [
               {'value': 'Enterprise', 'label': '企业监管',}
               ],
           }
        
        ]
    return permit


#1801	夏阳街道
#1802	盈浦街道
#1803	朱家角镇
#1804	练塘镇
#1805	金泽镇
#1806	赵巷镇
#1807	徐泾镇
#1808	华新镇
#1809	重固镇
#1810	白鹤镇
#1811	香花桥街道

site_cfg['permit.options'] = get_permit