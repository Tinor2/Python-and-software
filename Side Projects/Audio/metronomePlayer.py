from playsound import playsound
from time import sleep
def BPMtoSEC(bpm):
    sec = 60/bpm
    return sec
beat = False
while True:
    try:
        if beat == False:
            print("Start!")
            beat = True
        playsound("Audio/metronome.MP3")
        sleep(BPMtoSEC(100))
    except KeyboardInterrupt:
        print("")
        break