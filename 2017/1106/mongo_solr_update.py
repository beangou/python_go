#!/usr/bin/python
# -*- coding: UTF-8 -*-


import pymongo
import traceback
import sys
import urllib
import os

reload(sys)  
sys.setdefaultencoding('utf8')

conn = pymongo.MongoClient('mongodb://xxx_username:'+urllib.quote('xxx_pwd')+'@ip:port/xxx_db?authMechanism=SCRAM-SHA-1')
mongo_db = conn["spider_db"]
collection1 = mongo_db["collection_name1"]
collection2 = mongo_db["collection_name2"]
offset = 0
solr_host = 'ip:8983'

cursor = collection1.find(no_cursor_timeout=True)
for company in cursor:
	offset += 1
	print "当前第%s条" % (offset)
	try:
		thirdInfoList = company["thirdInfoList"]
    	# print "thirdInfoList %s" % thirdInfoList
		if len(thirdInfoList):
			for thirdInfo in thirdInfoList:
				if thirdInfo["platform"] == 3:
					hvCompanyId = thirdInfo["_id"]
					hVCompany = collection2.find_one({'_id': hvCompanyId})
					if hVCompany and hVCompany["sales"]:
						company["sales"] = hVCompany["sales"]
						update_result = collection1.update_one({'_id':company['_id']}, {"$set": company}, upsert=False)
						print "更新mongo成功条数：%s, companyId: %s" % (update_result.modified_count, company['_id'])
						cmd = ''' curl http://''' + solr_host + '''/solr/collection_name/update/\?commit\=true -H "Content-Type: text/xml" --data-binary '<add><doc><field name = "id">''' + company['_id'] + '''</field><field name ="sales" update="set">''' +hVCompany["sales"]+ '''</field></doc></add>' '''
						os.system(cmd)
						print "更新solr,companyId: %s" % (company['_id'])
						break
	except Exception as e:
		print "error: message=%s, company_id=%s" % (e, company['_id'])
cursor.close()

# insert mongo
# contacts_detail = {}
# contacts_detail["companyId"] = row_id
# contacts_detail["name"] = row_companyname
# contacts_detail["userId"] = row_user_id
# mongo_collection.insert(contacts_detail)