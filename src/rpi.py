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

####### Standards #######

GPIO.output(22, GPIO.LOW)

############ PROGRAMM ###################

letters = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

def morse():
    print('Text der gemorst wird:')
    nachricht = input()
    
    for char in nachricht:
        text = text + letters[char.upper()]
    
def morse_to_binary(mstring):
    st = 0
    while st < len(mstring):
    
        if mstring[st] == '.':
            GPIO.output(22, GPIO.HIGH)
            time.sleep(.02)
            GPIO.output(22, GPIO.LOW)
        elif mstring[st] == '-':
            GPIO.output(22, GPIO.HIGH)
            time.sleep(.04)
            GPIO.output(22, GPIO.LOW)
        st = st + 1
            
try:
    morse()

######### ERROR UND CLEANUP #############

except:
    print('ABBRUCH')
    
finally:
    GPIO.cleanup();
