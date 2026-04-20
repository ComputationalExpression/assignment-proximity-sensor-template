import machine
from machine import Pin
from time import sleep

class ProxSensor:

    def __init__(self):
        self.trigger = Pin(12, Pin.OUT)
        self.echo = Pin(13, Pin.IN)

    def pulse(self, times: int = 1) -> int:
        """ Takes a reading from the sensor; returns reading """
        reading += machine.time_pulse_us(self.echo, 1, 30000)
    
    def __toggle_sensor(self, sleep_s: float = 0) -> None:
        sleep(sleep_s)
        self.trigger.toggle()

