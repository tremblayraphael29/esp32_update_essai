from machine import Timer
from machine import Pin

index_rear_led = 0
led_rear_left = Pin(2, Pin.OUT)

print('Version 2 installed using USB') 

def index_ms():
    global index_rear_led
    index_rear_led += 1
    led(index_rear_led)
    if index_rear_led == 800:
        index_rear_led = 0

def led(i):
    global index_rear_led
    led_rear_left.on() if 0 < i < 50 else False
    led_rear_left.off() if 50 < i < 100 else False
    led_rear_left.on() if 100 < i < 150 else False
    led_rear_left.off() if 150 < i < 200 else False
    index_rear_led = 0 if index_rear_led == 800 else index_rear_led

tim0 = Timer(0)
tim0.init(period=10, mode=Timer.PERIODIC, callback=lambda t: index_ms())
