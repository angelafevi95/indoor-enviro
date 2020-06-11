from mq import*
import sys
import time
from mongoDB import mongoDB

database = mongoDB()
mq = MQ()

try:
    while True:
        records = database.records
        gasData =mq.MQPercentage()
        gasPayload = mq.MQallPercentage(gasData)

        database.exportData(gasPayload, records)
        time.sleep(10)

except KeyboardInterrupt:
    sys.exit(0)