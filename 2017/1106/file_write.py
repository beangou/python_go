#!/usr/bin/python
# -*- coding: UTF-8 -*-


import pymongo
import traceback
import sys
import urllib
import os
import json
from bson.objectid import ObjectId

reload(sys)
sys.setdefaultencoding('utf8')


# w+表示存在就覆盖，写入
fo = open("/home/xxx/xx_.json", "w+")
fo.write("文本内容")
# 关闭打开的文件
fo.close()