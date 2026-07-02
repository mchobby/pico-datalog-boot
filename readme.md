[This file also exists in ENGLISH](readme_ENG.md)

# Utiliser le Pico-DataLog-Boot avec MicroPython
Le Pico-Datalog-boot est une carte d'extension pour Pico équipé d'une horloge temps réelle (RTC: Reak Time Clock) et d'un connecteur microSD. 

![Pico-Datalog-boot](docs/_static/pico-datalog-boot.jpg)

Cette extension contient tout ce qu'il faut pour gérer le temps et le stockage de grands fichiers (lecture/écriture de fichiers sur une carte SD est vraiment un excellent complément sur un projet).

[Le schéma (r1) est disponible ici](docs/_static/pico-datalog-boot-schematic-r1.jpg)

# Installer depuis le MASTER

Le répertoire [masters.out/](masters.out) propose une archive ZIP contenant tous les fichiers nécessaires (scripts d'examples et bibliothèques). 

Faites une extraction des fichiers et copiez les sur votre plateforme MicroPython et "Voila !"... vous êtes prêt.

# Installer les bibliothèques

Les bibliothèques doivent être copiés sur votre carte MicroPython avant de tester les exemples.

Vous pouvez installer les bibliothèques depuis le __master__ ou en exécutant les commandes suivantes: 

Sur une plateforme WiFi :

```
>>> import mip
>>> mip.install("github:mchobby/esp8266-upy/pcf8523")
```

Ou via l'utilitaire mpremote :

```
mpremote mip install github:mchobby/esp8266-upy/pcf8523
```

Copier le fichier `sdscard.py` depuis le dépôt micropython-lib :

* [micropython-lib/micropython/drivers/storage/sdcard](https://github.com/micropython/micropython-lib/tree/master/micropython/drivers/storage/sdcard)

# Brancher

Connectez votre picro sur le Pico-Datalog-boot. Faites attention à placer le connecteur USB de votre Pico au dessus de la piile bouton.

![Installer Pico-Datalog-boot](docs/_static/pico-datalog-boot-install.jpg)

Note: le dessous de la carte Pico-DataLog-Boot reprend la mentions "USB" permettant d'indiquer l'orientation du Pico.

# Tester

Les bibliothèques doivent être installée avant l'exécution des scripts d'exemple.

A propos des examples:

Le sous-répertoire `examples` contient des scripts bien documentés.

* __[test_sd_detect.py](examples/test_sd_detect.py)__ : comment vérifier la présence de la carte microSD dans le connecteur.
* __[test_sd_mount.py](examples/test_sd_mount.py)__ : Comment monter/démonter la carte SD dans le système de fichiers MicroPython. L'exemple liste les fichiers dans présent dans le répertoire. En anglais, ces opérations s'appellent _mount/unmount_.
* __[test_getdate.py](examples/test_getdate.py)__ : Comment lire l'heure de l'horloge RTC
* __[test_setdate.py](examples/test_setdate.py)__ : Comment modifier l'heure de l'horloge RTC (cela doit bien être fait une fois).
* __[test_alarm.py](examples/test_alarm.py)__ : Experimentation avec la fonctionnalité d'alarme (de l'horloge RTC).
* __[test_attribute.py](examples/test_attribute.py)__ : Inspection des attributs de l'horloge RTC.
* __[test_clockout.py](examples/test_clockout.py)__ : produit un signal d'horloge sur la broche clkout/int. Les fréquences disponibles sont: 32768, 16384, 8192, 4096, 1024, 32, 1 Hz et None.
* __[test_wakeup.py](examples/test_wakeup.py)__ : réveille un Pico du mode lightsleep avec un interruption matérielle générée par le pcf8523 lors d'une alarme (signal tombant sur la broche clkout/int du pcf8523).

Il est vivement recommandé de lire ces scripts d'exemples pour découvrir les fonctionnalités.

# Liste d'achat
* [Pico-DataLog-Boot](https://shop.mchobby.be/fr/pico-rp2x/2912-carte-data-logger-pour-raspberry-pi-pico-3232100029125.html) est disponible @ MCHobby