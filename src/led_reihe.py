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


in1 = 17
in2 = 27
in3 = 25

out1 = 22
out2 = 23
out3 = 24
out4 = 25

#GPIOs Definieren
GPIO.setup(in1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Output
GPIO.setup(out1, GPIO.OUT)
GPIO.setup(out2, GPIO.OUT)
GPIO.setup(out3, GPIO.OUT)
GPIO.setup(out4, GPIO.OUT)

####### Standards #######

GPIO.output(out1, GPIO.LOW)
GPIO.output(out2, GPIO.LOW)
GPIO.output(out3, GPIO.LOW)
GPIO.output(out4, GPIO.LOW)

############ PROGRAMM ###################

try:
    while True:
        if (GPIO.input(in1)):
            print("Button 1 Pressed")
        if (GPIO.input(in2)):
            print("Button 2 Pressed")
        if (GPIO.input(in3)):
            print("Button 3 Pressed")
            
    
#    i = 0
#    while i<100:
#        print ('1')
#        GPIO.output(22, GPIO.HIGH)
#        time.sleep(0.1)
#        GPIO.output(22, GPIO.LOW)
#        print ('2')
#        GPIO.output(23, GPIO.HIGH)
#        time.sleep(0.1)
#        GPIO.output(23, GPIO.LOW)
#        print ('3')
#        GPIO.output(24, GPIO.HIGH)
#        time.sleep(0.1)
#        GPIO.output(24, GPIO.LOW)
#        print ('4')
#        GPIO.output(25, GPIO.HIGH)
#        time.sleep(0.1)
#        GPIO.output(25, GPIO.LOW)        
#        i = i + 1
#        time.sleep(.5)

######### ERROR UND CLEANUP #############

except:
    print('ABBRUCH')
    
finally:
    GPIO.cleanup();
