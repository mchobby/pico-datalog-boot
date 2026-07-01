# Using Pico-DataLog-Boot with MicroPython
The Pico-Datalog-boot is a Pico Expansion board fitting a RTC (Reak Time Clock) and a SDCard. 

![Pico-Datalog-boot](docs/pico-datalog-boot.jpg)

This expansion contains everything you need to deal with datetime and with large file storage (read/write files on a sd card is really great)

# Install from MASTER

The [masters.out/](masters.out) folder contains ZIP archive with all required files (examples scripts and libraries). Extract the files and copy them on your MicroPython plateform.

# Install the Libraries

The library must be copied on the MicroPython board before using the examples.

On a WiFi capable plateform:

```
>>> import mip
>>> mip.install("github:mchobby/esp8266-upy/pcf8523")
```

Or via the mpremote utility :

```
mpremote mip install github:mchobby/esp8266-upy/pcf8523
```

Copy the `sdscard.py` file from the micropython-lib repository:

* [micropython-lib/micropython/drivers/storage/sdcard](https://github.com/micropython/micropython-lib/tree/master/micropython/drivers/storage/sdcard)

# Wiring 

Just plug your Pico on the Pico-Datalog-boot. Take care to place the pico USB over the CR1220 cell coin.

# Testing

The required library must be installed prior to run the MicroPython examples scripts.

About examples:

The `examples` sub-folder contains well documented scripts.

It is a great idea to read them to discover the features.

# Shopping List
xxx