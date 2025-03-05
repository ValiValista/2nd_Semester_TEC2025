from time import sleep
from picozero import pico_led


while True():
    pico_led.on()
    sleep(1)
    pico_led.off()

