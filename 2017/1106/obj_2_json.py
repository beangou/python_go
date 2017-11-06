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

class ShipmentClz:
   '海关数据类'
 
   def __init__(self, _id, buyer):
      self.id = _id
      self.buyer = buyer

shipmentObj = ShipmentClz("111", "xxx")
#对象转化为字典
myClassDict = shipmentObj.__dict__
#打印字典
myClassJson = json.dumps(myClassDict)
print "json=%s" % myClassJson