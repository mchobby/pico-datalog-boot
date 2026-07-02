""" MicroPython driver for the PCF8523 RTC over I2C.

	Read the time from the RTC

	Dominique Meurisse for MCHobby.be - initial portage

"""
from machine import I2C, Pin
from pcf8523 import PCF8523
import time

# Raspberry-Pi Pico
i2c = I2C(1, sda=Pin(6), scl=Pin(7))
rtc = PCF8523( i2c )

_time = rtc.datetime
print( "Time: %s secs" % _time )
print( "Year: %s, month: %s, day: %s, hour: %s, min: %s, sec: %s, weekday: %s, yearday: %s" % time.localtime(_time) )

days = ['monday','tuesday', 'wednesday', 'thursday', 'friday', 'saterday', 'sunday' ]
weekday = time.localtime(_time)[6]
print( 'Day of week: %s' % days[weekday] )
