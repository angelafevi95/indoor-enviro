import csv
import math 
from datetime import datetime 
from mongoDB import mongoDB

## CSV Information about the monitored user. 
userData = 'SLEEP_USER1.csv'

class miband(): 

    def read_sleep_info(self):

        month = []
        with open(userData, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0

            for day in csv_reader:
                if line_count == 0:
                    print(f'Sleep data obtained is {", ".join(day)}')
                    line_count = +1

                payload = {
                    'datetimeSleep': day["date"],
                    'data': {
                        'sleepHours': self.getSleepHours(day["start"], day["stop"]),
                        'deepSleepHours': day["deepSleepTime"]/60,
                        'shallowSleepHours': day[["shallowSleepTime"]/60    
                    }
                }

                month.append(payload)

                
      return month

    def getSleepHours(self, start, stop):
        sleepSeconds = stop-start
        sleepHours   =  datetime.fromtimestamp(sleepSeconds)    
    
        return sleepHours 


mibandata = miband()
database  = mongoDB()

monthlyInfo = mibandata.read_sleep_info()
records = database.records
database.exportData(monthlyInfo, records)