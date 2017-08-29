# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

############# IMPORTS ################

#GPIO Port Libaries importieren
import RPi.GPIO as GPIO
import time
import threading

############ RPi-SETTINGS ###############
#Boardmodus setzen
GPIO.setmode(GPIO.BCM)


in1 = 17
in2 = 27
in3 = 16

out1 = 22   #White1
out2 = 23   #White2
out3 = 24   #Blue1
out4 = 25   #Blue2
out5 = 26   #Button Green
out6 = 13   #Signal Yellow
out7 = 12   #Signal Red


#GPIOs Definieren
GPIO.setup(in1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Output
GPIO.setup(out1, GPIO.OUT)#White1
GPIO.setup(out2, GPIO.OUT)#White2
GPIO.setup(out3, GPIO.OUT)#Blue1
GPIO.setup(out4, GPIO.OUT)#Blue2

GPIO.setup(out5, GPIO.OUT) #Button LED

GPIO.setup(out6, GPIO.OUT) #Signal Yellow
GPIO.setup(out7, GPIO.OUT) #Signal Red

####### Standards #######
GPIO.output(out1, GPIO.LOW)
GPIO.output(out2, GPIO.LOW)
GPIO.output(out3, GPIO.LOW)
GPIO.output(out4, GPIO.LOW)
GPIO.output(out5, GPIO.LOW)
GPIO.output(out6, GPIO.LOW)
GPIO.output(out7, GPIO.LOW)

############ PROGRAMM ###################
class busy(threading.Thread,prg_ok):
    
    def __init__(self, thread_number):
        threading.Thread.__init__(self)
        self.thread_number = thread_number
    def run(self,prg_ok):
	if prg_ok == False:
            GPIO.output(out6, GPIO.HIGH)
            time.sleep(0.02)
            GPIO.output(out6, GPIO.LOW)
        elif prg_ok == True:
            GPIO.output(out6, GPIO.LOW)
    
 try:
    jobs=[]
    while True:
        if (GPIO.input(in1)):
            GPIO.output(out5,1)
            print("Button 1 Pressed")
            time.sleep(0.5)
            jobs.append(busy(False))
            GPIO.output(out5,0)
            
        if (GPIO.input(in2)):
            GPIO.output(out5,1)
            print("Button 2 Pressed")
            jobs.pop()
            time.sleep(0.5)
            GPIO.output(out5,0)
            
        if (GPIO.input(in3)):
            GPIO.output(out5,1)
            print("Button 3 Pressed")
            time.sleep(0.5)
            GPIO.output(out5,0)
    
    for job in jobs: # Wait for the background task to finish
        job.join()       
    print 'Main program waited until background was done.'

######### ERROR UND CLEANUP #############

except:
    print('ABBRUCH')
    
finally:
    GPIO.cleanup();
