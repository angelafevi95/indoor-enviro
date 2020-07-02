import csv
import math 

## CSV Information about the monitored user. 
userData = 'SLEEP_USER1.csv'

class miband(): 

    def read_sleep_info(self):
        with open(userData, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0

            month = []

            for day in csv_reader:
                if line_count == 0:
                    print(f'Sleep data obtained is {", ".join(day)}')
                    line_count = +1

                payload = {
                    'datetime': day["date"],
                    'data': {
                        'sleepHours': self.getSleepHours(day["start"], day["stop"]),
                        'deepSleepHours': day["deepSleepTime"]/60,
                        'shallowSleepHours': day[["shallowSleepTime"]/60    
                    }
                }

                month.append(payload)

        return month
    # https://realpython.com/python-csv/
    
    def getSleepHours(self, start, stop):
        sleepSeconds = stop-start
        sleepHours   =         # transform from time stamp

        return sleepHours 

mibandata = miband()

mibandata.read_sleep_info()