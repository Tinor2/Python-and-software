from machine import Pin, PWM
from utime import sleep

onPin = Pin(15,Pin.OUT)
onPin.value(1)
sensor = Pin(0, Pin.IN, Pin.PULL_UP)
light = Pin(1,Pin.OUT)
motor = PWM(Pin(2,Pin.OUT))
i = 0
while True:
    try:
        for duty in range(65025):
            motor.duty_u16(duty)
            sleep(0.0001)
        for duty in range(65025, 0, -1):
            motor.duty_u16(duty)
            sleep(0.0001)
        if sensor.value() == 0:
            i+=1
            print("Sound Detected for the",str(i)," time")
            light.value(1)
            sleep(0.1)
        else:
            light.value(0)
    except KeyboardInterrupt:
        onPin.value(0)
        break
