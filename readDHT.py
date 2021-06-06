
#!/usr/bin/python
import sys
import Adafruit_DHT
import asyncio
from kasa import SmartPlug

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print ('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))

    plug = SmartPlug("91.0.0.1")

    if humidity >= 50.0:
        plug.turn_off() # if the humidity is above 50.0% the plug should turn off. 
        if humidity <= 20.0:
            plug.turn_on() # if the humidity is below 20.0% the plug should turn on. 
