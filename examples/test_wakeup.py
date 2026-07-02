""" MicroPython driver for the PCF8523 RTC over I2C.

    Test microcontroler WAKE-UP feature on GPIO IRQ.
	An RTC alarm is set to now + 30 sec for waking up the MCU

	Note:
	 * clk_int jumper must be closed.
	 * INT will be kept HIGH with input pull-up. 
	   pcf8523 clkout/int will go LOW on alarm.
	   Code will have to reset pcf8523 intrrupt for clkout/int to go HIGH again.

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

# Get the current time
now = rtc.datetime
print( "now   @ Year: %s, month: %s, day: %s, hour: %s, min: %s, sec: %s, weekday: %s, yearday: %s" % time.localtime(now) )

# Calculate Alarm 1 minute in the future
alarm_time = now + 60
alarm_tuple = time.localtime(alarm_time) # Year, month, day, hour, min, sec, weekday, yearday
alarm_minutes = alarm_tuple[4]

# set the alarm for activerate every hour & <alarm_min>
rtc.alarm_weekday( enable=False )
rtc.alarm_day    ( enable=False )
rtc.alarm_hour   ( enable=False )
rtc.alarm_min( alarm_minutes, True )

# Re-read alarm setting
print( "alarm_wday:", rtc.alarm_weekday() )
print( "alarm_day :", rtc.alarm_day() )
print( "alarm_hour:", rtc.alarm_hour() )
print( "alarm_min :", rtc.alarm_min() )

# Activate PCF8523 interrupt pin on alarm. Quite handy to wake-up a microcontroler
#  Interrupt pin goes to 3.3V on alarm
print( "setting alarm interrupt")
#rtc.clear_interrupt()
rtc.clock_out = None # Disable Clock-Out on clkout/int
rtc.clear_interrupt() # Clear any existing alarm
rtc.alarm_interrupt = True # Activate interrupt on alarm


print( "Configure Wakeup Pin")
def do_wake_up(pin):
	# Light up the LED on wake up
	Pin('LED', Pin.OUT, value=1 )

gp5 = Pin(5, Pin.IN, Pin.PULL_UP )
gp5.irq(trigger=Pin.IRQ_FALLING, handler=do_wake_up) # wake param not yet supported for RP2

# wfi puts the pico into a suspended state 
# until any interrupt is received
@micropython.asm_thumb
def _lightsleep():
    wfi()

# Put the Pico into deep sleep
print("Entering light sleep...")
# must wait a bit to send the message otherwise 
# seritma interrupt will immediately wakeup the MCU
time.sleep_ms( 200 )
_lightsleep()

# Can only be seen when MCU is wake-up
print("Wake-Up from Light Sleep")
# Reset interrupt state
rtc.clear_interrupt() 

print( "That's all folks!")
