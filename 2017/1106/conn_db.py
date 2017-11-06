#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import pymongo
import json
import traceback
import sys


reload(sys)
sys.setdefaultencoding('utf8')

# 打开数据库连接
db = MySQLdb.connect("ip","username","password","dbname" )
# 使用cursor()方法获取操作游标
cursor = db.cursor()

parsed_json = None
row_id = None
offset = 0
limit = 100
try:
  while True:
      # 使用execute方法执行SQL语句
	  sql = "select * from t_xxx a where a.xx = %d" % (10)
	  cursor.execute(sql)
	  rowCount = cursor.rowcount
	  results = cursor.fetchall()
	  i = -1
	  for index in range(len(results)):
	    i += 1
	    i %= 2
	    if i != 0:
	      continue
	    first_line = results[index]
	    second_line = results[index+1]
	    first_parsed_json = json.loads(first_line[6])
	    seconde_parsed_json = json.loads(second_line[6])
	    first_str = first_parsed_json["toUpdateFields"]
	    second_str = seconde_parsed_json["toUpdateFields"]
	    first_row_id = results[index][0]
	    second_row_id = results[index+1][0]
	    if (first_str == second_str):
	    	print "%s,%s," % (first_row_id, second_row_id)
	  if rowCount < 100:
	    print "break rowCount=%s" % rowCount
	    break
	  offset += limit
except Exception as e:
  print "error: unable to fetch data, message=%s, parsed_json=%s, row_id=%s" % (e, parsed_json, row_id)


# sql = "INSERT INTO `xxx` (`USER_ID`, `PERSON_ID`) VALUES ('6cde819c9f914e2e8aad472af5ed1c72', '1d0bb0c1059946c288b479dc9d3ebb26')";
# 	cursor.execute(sql)
# 	db.commit()
# 	cursor.close()


# 关闭数据库连接
db.close()

