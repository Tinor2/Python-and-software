#Reading analogue input
from machine import Pin, ADC
from utime import sleep
import math
green = ADC(28)
i = 0
c= 0
onLight = Pin("LED",Pin.OUT)
onLight.value(1)

previousReading = green.read_u16()
for i in range(100):
    sleep(0.05)
    reading = green.read_u16()
    previousReading = (reading +previousReading)/2
zero = previousReading
print(zero)
maxValue = 0
i = 0
thresh = 500
threshedValue = 0
while True:
    i += 0.1
    sleep(0.05)
    reading = green.read_u16()
    reading = reading - zero
    reading = round(reading,-2)
    if (reading-zero) <= 50:
        reading = 0
    elif maxValue < reading:
        maxValue = reading
        if maxValue >= 25000:
            maxValue = 25000
    if reading >= maxValue:
        reading = maxValue
    if reading >= thresh:
        threshedValue = 1
    else:
        threshedValue = 0
    print(threshedValue)
    

    print(reading)
    