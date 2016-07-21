#!/usr/bin/python
from astro_pi import AstroPi
import time

ap = AstroPi()
temp = ap.get_temperature()
humidity = ap.get_humidity()
pressure = ap.get_pressure()


print("Temperature: %s C" % temp)               # Show temp on console
print("Humidity: %s %%rH" % humidity)        # Show humidity on console
print("Pressure: %s Millibars" % pressure)    # Show pressure on console

ap.set_rotation(180)        # Set LED matrix to scroll from right to left
              
ap.show_message("Temperature: %.2f C" % temp, scroll_speed=0.05, text_colour=[0, 255, 0])

time.sleep(1)           # Wait 1 second

ap.show_message("Humidity: %.2f %%rH" % humidity, scroll_speed=0.05, text_colour=[255, 0, 0]) 

time.sleep(1)      # Wait 1 second

ap.show_message("Pressure: %.2f Millibars" % humidity, scroll_speed=0.05, text_colour=[0, 0, 255])

ap.clear()      # Clear LED matrix
