import sys
import time

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


## Pimori Enviro object: temperature, humidity, pressure, light

class enviro():

    factor          = 2.5
    
    bus             = SMBus(1)
    bme280          = BME280(i2c_dev=bus)
    ltr559          = LTR559()

    # Get the temperature of the CPU for compensation
    
    def get_cpu_temperature(self):
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = f.read()
            temp = int(temp) / 1000.0
        return temp

    cpu_temps       = [self.get_cpu_temperature()] * 5
    
    def get_weather(self):

        cpu_temp = self.get_cpu_temperature()
        # Smooth out with some averaging to decrease jitter
        self.cpu_temps = self.cpu_temps[1:] + [self.cpu_temp]
        avg_cpu_temp = sum(self.cpu_temps) / float(len(self.cpu_temps))
        raw_temp = bme280.get_temperature()
        comp_temp = raw_temp - ((avg_cpu_temp - raw_temp) / self.factor)

        pressure        = bme280.get_pressure()
        humidity        = bme280.get_humidity()

        return comp_temp, pressure, humidity

    def get_light(self):

        lux             = ltr559.get_lux()
        #proximity      = ltr559.getproximity()
        return lux 

    def get_all_sensors_data(self):
        # while True:
            temp, press, hum = self.get_weather()
            lux = self.get_light()

            payload = {
                'timestamp': time.time(),
                'data': {
                    'temeprature': temp,
                    'pressure': press,
                    'humidity' : hum, 
                    'light': lux
                }
            }


