# Pico-DataLog-Boot - Mount the SD Card
#
# See project: https://github.com/mchobby/pico-oled-boot
#
from machine import Pin, SPI
from os import VfsFat, mount, umount, listdir
from sdcard import SDCard

spi = SPI( 1, sck=Pin(10), mosi=Pin(11), miso=Pin(8), baudrate=0x14<<20)
cs = Pin(9,Pin.OUT, value=True )
sd_card = SDCARD( spi, cs )
vfs = VfsFat(sd_card)
mount( vfs, "/sd" )

print( 'dir /', os.listdir() )
print( 'dir /sd', os.listdir('/sd') )

# unmount the SD Card
umount( "/sd" )