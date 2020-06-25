from mongoDB import mongoDB
from enviro import enviro

import time
import sys

"""
This scripts requieres the addition of mongoDB and enviro objects.
It uses the weather measures obtained from the sensors and uploads it into MongoDB Atlas collection. 

"""

database    = mongoDB()
sensors     = enviro()

try:
    while True:
        records = database.records
        sensorsData = sensors.get_all_sensors_data()

        database.exportData(sensorsData, records)
        time.sleep(900)

except KeyboardInterrupt:
    sys.exit(0)
