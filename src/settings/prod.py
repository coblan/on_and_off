from .base import *
import sys

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'on_and_off',
        'USER': 'root',
        'PASSWORD': 'root533',
        'HOST': '127.0.0.1', 
        'PORT': '5432', 
    },
}

#DATA_PROXY ={
    #'http': 'socks5://localhost:10899',
#} 

SANGO_BRIDGE='http://12.110.185.17:8499'
SANGO_BRIDGE='http://10.231.18.23:8499'


INFO_SERVICE = 'http://10.235.243.190:8006/manainf/services/infoService/getEntyBasicInfoList' # getEntyBasicInfo'

#DEV_STATUS='dev'

#GDAL_LIBRARY_PATH = r'C:\Program Files\GDAL\gdal202'

ALLOWED_HOSTS = ['10.231.18.23']

import os
LOG_PATH= os.path.join( os.path.dirname(BASE_DIR),'log')

LOGGING = {
    'version': 1, # 标示配置模板版本，int 类型，目前只接收 `1`这个值。
    'disable_existing_loggers': False, 
    'formatters': {
        'standard': {
             'format': '%(levelname)s %(asctime)s %(message)s',
        },
    },
    'filters': {
        # 这里是定义过滤器，需要注意的是，由于 'filters' 是 logging.config.dictConfig 方法要求在配置字典中必须给订的 key ,所以即使不使用过滤器也需要明确给出一个空的结构。
    },
    'handlers': {
         'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter':'standard',
        },
        'rotfile':{
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024*1024*5,
            'backupCount':3,
            'formatter':'standard',
            'filename': os.path.join(LOG_PATH,'task.log'),            
            }, 
        'caseFile':{
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024*1024*5,
            'backupCount':3,
            'formatter':'standard',
            'filename': os.path.join(LOG_PATH,'case_file.log'),            
            }, 
        'console': {
            'level':'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
            },  
        'djangoout':{
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024*1024*5,
            'backupCount':3,
            'formatter':'standard',
            'filename': os.path.join(LOG_PATH,'django.log'),            
            },         
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'djangoout', 'mail_admins'],
            'level': 'ERROR',
            },        
        'manage_task':{
            'handlers': ['console', 'rotfile'],
            'level': 'DEBUG',
            'propagate': True,            
        },
        #'django.request': {
            #'handlers': ['rotfile'],
            #'level': 'ERROR',
            #'propagate': True,
        #},        
    }
}