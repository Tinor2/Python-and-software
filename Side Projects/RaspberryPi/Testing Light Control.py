from machine import Pin, PWM

red = PWM(Pin(1))
blue = PWM(Pin(3))
green = PWM(Pin(2))

 
red.freq(1000)
blue.freq(1000)
green.freq(1000)

maxValue = 65500

red.duty_u16(int(maxValue*0.01))
#blue.duty_u16(int(maxValue*1))
#red.duty_u16(int(maxValue*1))