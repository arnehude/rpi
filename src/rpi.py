# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

############# IMPORTS ################

#GPIO Port Libaries importieren
import RPi.GPIO as GPIO
import time as time

############ RPi-SETTINGS ###############
#Boardmodus setzen
GPIO.setmode(GPIO.BCM)

#GPIOs Definieren
#Output
GPIO.setup(22, GPIO.OUT)

####### Standards #######

GPIO.output(22, GPIO.LOW)

############ PROGRAMM ###################

try:
    i = 0
    while i<5:
        x = 0
        while x < 10:
            GPIO.output(22, GPIO.HIGH)
            time.sleep(.2)
            GPIO.output(22, GPIO.LOW)
            time.sleep(.2)
            x = x + 1
        i = i + 1
        print('Durchgang: ', i)
        time.sleep(1)

######### ERROR UND CLEANUP #############

except:
    print('ABBRUCH')
    
finally:
    GPIO.cleanup();
