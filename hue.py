#!/usr/bin/ python

from phue import Bridge
from time import sleep
from Adafruit_CharLCD import Adafruit_CharLCD
import Adafruit_BBIO.GPIO as GPIO

pin1 = "P8_14"
pin2 = "P8_16"
pin3 = "P8_11"
pin4 = "P9_13"
pin5 = "P9_12"
pin6 = "P9_26"
pin7 = "P9_11"

def getKey():

    KEYPAD = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ["*",0,"#"]
    ]
    
    ROW = [pin7, pin6, pin5, pin4]
    COLUMN = [pin3, pin2, pin1]

    # Set all columns as output low
    for j in range(0,3):
        GPIO.setup(COLUMN[j], GPIO.OUT)
        GPIO.output(COLUMN[j], GPIO.LOW)
     
    # Set all rows as input
    for i in range(0,4):
        GPIO.setup(ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
     
    # Scan rows for pushed key/button
    # A valid key press should set "rowVal" between 0 and 3.
    rowVal = -1
    while rowVal == -1:
        for i in range(0,4):
            tmpRead = GPIO.input(ROW[i])
            if tmpRead == 0:
                rowVal = i

    # Convert columns to input
    for j in range(0,3):
        GPIO.setup(COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)
     
    # Switch the i-th row found from scan to output
    GPIO.setup(ROW[rowVal], GPIO.OUT)
    GPIO.output(ROW[rowVal], GPIO.HIGH)
 
    # Scan columns for still-pushed key/button
    # A valid key press should set "colVal"  between 0 and 2.
    colVal = -1
    while colVal == -1:
        for j in range(0,3):
            tmpRead = GPIO.input(COLUMN[j])
            if tmpRead == 1:
                colVal=j
    
    return KEYPAD[rowVal][colVal]
 
button = None

# Initialize Bridge
try:
    b = Bridge('10.1.2.162')
    lights_list = b.get_light_objects('list')
except IOError:
    sleep(60)
    b = Bridge('10.1.2.162')
    lights_list = b.get_light_objects('list')
    
# Default Startup to 2700K
B2700 = {"on":True, "xy":[0.4370,0.3706],"bri":254}
W2700 = {"on":True, "xy":[0.4581,0.3990],"bri":254}

b.set_light(2, B2700)
b.set_light(1, W2700)

while button == None:
    button = getKey()
    sleep(0.2)

    if button == 1:
        B2700 = {"on":True, "xy":[0.4370,0.3706],"bri":254}
        W2700 = {"on":True, "xy":[0.4581,0.3990],"bri":254}

        b.set_light(2, B2700)
        b.set_light(1, W2700)
        
    elif button == 2:
        B3000 = {"on":True, "xy":[0.4142,0.3616],"bri":254}
        W3000 = {"on":True, "xy":[0.4339,0.3925],"bri":254}

        b.set_light(2, B3000)
        b.set_light(1, W3000)

    elif button == 3:
        B3500 = {"on":True, "xy":[0.3910,0.3600],"bri":254}
        W3500 = {"on":True, "xy":[0.3994,0.3770],"bri":254}

        b.set_light(2, B3500)
        b.set_light(1, W3500)

    elif button == 4:
        B4100 = {"on":True, "xy":[0.3699,0.3688],"bri":254}
        W4100 = {"on":True, "xy":[0.3690,0.3620],"bri":254}

        b.set_light(2, B4100)
        b.set_light(1, W4100)

    elif button == 5:
        B5000 = {"on":True, "xy":[0.3378,0.3528],"bri":254}
        W5000 = {"on":True, "xy":[0.3371,0.3400],"bri":254}

        b.set_light(2, B5000)
        b.set_light(1, W5000)

    elif button == 0:
        for light in lights_list:
            light.on = False
    
    button = None