""" MicroPython driver for the PCF8523 RTC over I2C.

    Generate a 1024 Hz on ClkOut/Int pin.

    On my setup clk_int jumper was solderer (so connected to GP5)
    I did also check the waveform with scope.

	Dominique Meurisse for MCHobby.be - initial portage
"""
from machine import I2C,Pin,idle
from pcf8523 import PCF8523
import time

# Light OFF user LED
Pin('LED', Pin.OUT, value=0 )

# Raspberry-Pi Pico - GP6=sda, GP7=scl
i2c = I2C(1, sda=Pin(6), scl=Pin(7))
rtc = PCF8523( i2c )

# Pull-up is recommanded on clkout/int pin of pcf8523 
# but seems to work witout it!

gp5 = Pin(5, Pin.IN ) #, Pin.PULL_UP )
rtc.clock_out = 1024 # change default clock_out 32537 Hz to 1024 Hz
