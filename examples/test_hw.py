# Pico-DataLog-Boot - Hardware test 
#
# See project: https://github.com/mchobby/pico-oled-boot
#
from machine import I2C, Pin
from pcf8523 import PCF8523
import time

i2c = I2C(1, sda=Pin(6), scl=Pin(7))
print( "I2C Scan:", i2c.scan() )
rtc = PCF8523( i2c )
_time = rtc.datetime
print( "Time: %s secs" % _time )
print( "Year: %s, month: %s, day: %s, hour: %s, min: %s, sec: %s, weekday: %s, yearday: %s" % time.localtime(_time) )

days = ['monday','tuesday', 'wednesday', 'thursday', 'friday', 'saterday', 'sunday' ]
weekday = time.localtime(_time)[6]
print( 'Day of week: %s' % days[weekday] )

