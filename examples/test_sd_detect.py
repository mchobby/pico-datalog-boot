# Pico-DataLog-Boot - SD Card Detect
#
# See project: https://github.com/mchobby/pico-oled-boot
#
from machine import Pin

sd_detect = Pin( 12, Pin.IN )

if sd_detect.value():
	print( 'No SD Card')
else:
	print( 'SD Card Inserted!' )