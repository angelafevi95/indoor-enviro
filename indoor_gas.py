from mq import*
import sys
import time
from mongoDB import mongoDB

"""  
This Script requieres de used of mq library. 
It measures gas using the library and uploads a document into the collection chosen.

It measure is performed every 15'

"""

database = mongoDB()
mq = MQ()

try:
    while True:
        records = database.records
        gasData =mq.MQPercentage()
        gasPayload = mq.MQallPercentage(gasData)

        database.exportData(gasPayload, records)
        time.sleep(900)

except KeyboardInterrupt:
    sys.exit(0)