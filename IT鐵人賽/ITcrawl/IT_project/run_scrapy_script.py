import os
import time
import datetime
from datetime import date, timedelta

today = str(datetime.date.today() + timedelta(0) )

cmd = 'scrapy crawl athleta -o ' + today + '-athleta.csv'
print(cmd)
os.system(cmd)
