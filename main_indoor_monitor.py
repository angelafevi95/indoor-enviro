from mongoDB import mongoDB
from enviro import enviro

import time
import sys

#### SUPER TO DO:

##Create MongoDB class
##Create a dict using Enviro readings by returning variables from Enviro get_all_sensors_data()
# Test code
# Clean code
# check Mongo
# Data analysis

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
