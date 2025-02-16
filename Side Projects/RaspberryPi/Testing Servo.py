from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(11))
button = Pin(0,Pin.IN)
hallEffect = Pin(1,Pin.IN)
pwm.freq(1000)

while True:
    if button.value() ==1:
        for duty in range(65025):
            pwm.duty_u16(duty)
            sleep(0.0001)
        for duty in range(65025, 0, -1):
            pwm.duty_u16(duty)
            sleep(0.0001)
    if hallEffect.value() == 0:
        print("Magnet!")
    else:
        pwm.duty_u16(0)