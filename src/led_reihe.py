# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

############# IMPORTS ################

#GPIO Port Libaries importieren
import RPi.GPIO as GPIO
import time

############ RPi-SETTINGS ###############
#Boardmodus setzen
GPIO.setmode(GPIO.BCM)

#GPIOs Definieren
#Output
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

####### Standards #######

GPIO.output(22, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(25, GPIO.LOW)

############ PROGRAMM ###################

try:
    i = 0
    while i<100:
        print ('1')
        GPIO.output(22, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(22, GPIO.LOW)
        print ('2')
        GPIO.output(23, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(23, GPIO.LOW)
        print ('3')
        GPIO.output(24, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(24, GPIO.LOW)
        print ('4')
        GPIO.output(25, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(25, GPIO.LOW)        
        i = i + 1
        time.sleep(.5)

######### ERROR UND CLEANUP #############

except:
    print('ABBRUCH')
    
finally:
    GPIO.cleanup();
