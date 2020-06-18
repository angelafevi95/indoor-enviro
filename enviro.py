import sys
import time
import datetime

##BME280 weather sensor

from bme280 import BME280

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

try:
    from ltr559 import LTR559
except ImportError:
    import ltr559

from datetime import datetime

## Pimori Enviro object: temperature, humidity, pressure, light

class enviro():

    def __init__(self):
        self.factor          = 2.5
        self.cpu_temps       = [self.get_cpu_temperature()] * 5
        self.bus             = SMBus(1)
        self.bme280          = BME280(i2c_dev=self.bus)
        self.ltr559          = LTR559()

    # Get the temperature of the CPU for compensation
    
    def get_cpu_temperature(self):
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = f.read()
            temp = int(temp) / 1000.0
        return temp

    def get_weather(self):

        cpu_temp = self.get_cpu_temperature()
        # Smooth out with some averaging to decrease jitter
        self.cpu_temps = self.cpu_temps[1:] + [cpu_temp]
        avg_cpu_temp = sum(self.cpu_temps) / float(len(self.cpu_temps))
        raw_temp = self.bme280.get_temperature()
        comp_temp = raw_temp - ((avg_cpu_temp - raw_temp) / self.factor)

        pressure        = self.bme280.get_pressure()
        humidity        = self.bme280.get_humidity()
        
        return comp_temp, raw_temp, pressure, humidity

    def get_light(self):

        lux             = self.ltr559.get_lux()
        #proximity      = ltr559.getproximity()
        return lux 

    def get_all_sensors_data(self):
        comp_temp, raw_temp, press, hum = self.get_weather()
        lux = self.get_light()

        payload = {
            'datetime': datetime.fromtimestamp(time.time()),
            'timestamp': time.time(),
            'data': {
                'comp temeprature': comp_temp,
                'tempeparute':raw_temp,
                'pressure': press,
                'humidity' : hum, 
                'light': lux
            }
        }
        return payload


