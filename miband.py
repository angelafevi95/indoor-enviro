import csv
import math 
from datetime import datetime 
from mongoDB import mongoDB

## CSV Information about the monitored user. 
userData = 'SLEEP_DATA.csv'

class miband(): 

    def read_sleep_info(self):
        collectionSleep = {}
        month = []
        with open(userData, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0

            for day in csv_reader:
                if line_count == 0:
                    print(f'Sleep data obtained is {", ".join(day)}')
                    line_count = +1
                
                else:
                    deepHours = int(day['deepSleepTime'])/60
                    shallowHours =  int(day['shallowSleepTime'])/60

                    collectionSleep = {
                        'datetimeSleep': day['date'],
                        'sleepHours':self.getSleepHours(day['start'], day['stop']),
                        'deepSleepHours':deepHours,
                        'shallowSleepHours': shallowHours }

                    month.append(collectionSleep)

                
        return month

    def getSleepHours(self, start, stop):
        sleepSeconds = int(stop)- int(start)
        sleepHours   =  (sleepSeconds/60)/60
        print(sleepHours)
        return sleepHours 


mibandata = miband()
database  = mongoDB()

monthlyInfo = mibandata.read_sleep_info()
records = database.records

for day in monthlyInfo:
    database.exportData(day, records)

print("yata")