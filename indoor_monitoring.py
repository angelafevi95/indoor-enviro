import sys
import time
import loggin 

##BME280 weather sensor

from bme280 import BME280

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

##LTR559 light

import ltr559 

 ### GET DATA 
# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
        temp = int(temp) / 1000.0
    return temp

#Tuning factor for compensation
factor= 2.5 
cpu_temps = [get_cpu_temperature()] * 5

try:
    while True:

        ##BME280 weather sensor
        bus             = SMBus(1)
        bme280          = BME280(i2c_dev=bus)

        # temperature     = bme280.get_temperature()
        cpu_temp = get_cpu_temperature()
        # Smooth out with some averaging to decrease jitter
        cpu_temps = cpu_temps[1:] + [cpu_temp]
        avg_cpu_temp = sum(cpu_temps) / float(len(cpu_temps))
        raw_temp = bme280.get_temperature()
        comp_temp = raw_temp - ((avg_cpu_temp - raw_temp) / factor)

        pressure        = bme280.get_pressure()
        humidity        = bme280.get_humidity()

        print("Temperature", comp_temp)
        print("Pressure", pressure)
        print("Humidity", humidity)

        ##LTR559 light
        lux             = ltr559.get_lux()
        #proximity      = ltr559.getproximity()

        print("Lux", lux)


except KeyboardInterrupt:
    sys.exit(0)

