import pymongo
from bson.objectid import ObjectId
from dateutil import parser
import datetime
import time

dateStr = datetime.datetime.now().isoformat()
myDatetime = parser.parse(dateStr)



myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# myclient = pymongo.MongoClient('mongodb://user:password@example:port/smart-data-center')
mydb = myclient["smart-data-center"]
mycol = mydb["cameraPower"]

# cameraPower table
# camera_power_total_today = 250.32
datetime = '2020-02-14'
camera_power_consumption = 859
camera_power_total_today = 327621
camera_power_total_Yesterday = 326762


camera_power_total = mycol.find_one({'_id': ObjectId('5e22e1cdca9b75c0d72edd8a')},{ "_id": 0})
# camera_power_total_Yesterday = camera_power_total['camera_power_total_today']
# camera_power_consumption = camera_power_total_today - camera_power_total_Yesterday

##insert 一般資料
mydict = { "camera_power_consumption": camera_power_consumption, 'datetime':myDatetime}
# mydict = { "camera_power_total": camera_power_total}
x = mycol.insert_one(mydict)


##update 每日通報消耗度數
# cameraPower = 20.32
# myquery = { "_id": ObjectId('5d4d99f3512a1d796e6cd52f')}
# newvalues = { "$set": { "cameraPower": cameraPower } }
# mycol.update_one(myquery, newvalues)
##查看 data 每日通報消耗
# for x in mycol.find({"_id": ObjectId('5d4d99f3512a1d796e6cd52f')},{ "_id": 0}):
#     print(x)


##update cameraPower data 消耗
# myquery = { "_id": ObjectId('5e22e1cdca9b75c0d72edd8a')}
# newvalues = { "$set": { 
#                     "camera_power_total_today": camera_power_total_today,
#                     "camera_power_total_Yesterday":camera_power_total_Yesterday,
#                     "camera_power_consumption":camera_power_consumption,
#                     "datetime": myDatetime
#                     }
#                 }
# mycol.update_one(myquery, newvalues)

##查看 cameraPower
# for x in mycol.find({'_id': ObjectId('5e22e1cdca9b75c0d72edd8a')},{ "_id": 0}):
#     print(x)


##搜尋
# x = mycol.find_one()
# print(x)