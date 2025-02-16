from machine import Pin, ADC
from utime import sleep

sound = Pin(1,Pin.IN)

while True:
    sleep(0.015)
    print(sound.value())