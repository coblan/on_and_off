from helpers.director.shortcut import model_to_name, model_full_permit, add_permits, model_read_permit
from .models import * 

permits = [
    ('taskinfo', model_read_permit(TTaskinfo), model_to_name(TTaskinfo), 'model'), 
    ('street.1801.case', '', '', 'single' ),
    ('street.1802.case', '', '', 'single' ),
    ('street.1803.case', '', '', 'single' ),
    ('street.1804.case', '', '', 'single' ),
    ('street.1805.case', '', '', 'single' ),
    ('street.1806.case', '', '', 'single' ),
    ('street.1807.case', '', '', 'single' ),
    ('street.1808.case', '', '', 'single' ),
    ('street.1809.case', '', '', 'single' ),
    ('street.1810.case', '', '', 'single' ),
    ('street.1811.case', '', '', 'single' ),
    
    ('Enterprise', model_read_permit(Enterprise), model_to_name(Enterprise), 'model'), 
    
    ]


#{'label': '朱家角镇', 'value': '1803',}, 
#{'label': '华新镇', 'value': '1808',}, 
#{'label': '白鹤镇', 'value': '1810',}, 
#{'label': '香花桥街道', 'value': '1811',}, 

add_permits(permits)

