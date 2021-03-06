#První verze meteostanice, nefunkční venkovní teplota a přeskakování displeje 

from lcd_display import lcd
import RPi.GPIO as GPIO
import time
import dht11
import os

file = open("id.txt", "r")
id = file.read()
id = id[:-1]

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.cleanup()

cidlo = dht11.DHT11(pin = 11)
displej = lcd()

displej.display_string("Nacitam data", 1)

while (1):
        data = cidlo.read()
	if data.is_valid():
		teplota = data.temperature
		vlhkost = data.humidity

		adresa = "https://ioe.zcu.cz/th.php?id=" + str(id) + "&temperature=" + str(teplota) + "&humidity=" + str(vlhkost)
				
		os.system('curl "' + adresa + '"') 

                displej.display_string("Teplota je: %d C " % teplota, 1)
                displej.display_string("Vlhkost je: %d %%" % vlhkost, 2)
		print("Update")
		time.sleep(120)
	time.sleep(1)
