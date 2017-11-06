#!/usr/bin/python
# -*- coding: UTF-8 -*-


import pymongo
import traceback
import sys
import urllib
import os
import redis

reload(sys)  
sys.setdefaultencoding('utf8')

r = redis.Redis(host='ip',port=6379,password='password',db=0)
r.lpush('list_name','sss&&ddd')
