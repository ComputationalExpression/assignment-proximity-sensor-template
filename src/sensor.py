import machine
from machine import Pin
from time import sleep

class ProxSensor:

    def __init__(self):
        self.trigger = Pin(12, Pin.OUT)
        self.echo = Pin(13, Pin.IN)

    def pulse(self, times: int = 1) -> float:
        reading = 0
        for _ in range(times):
            self.__toggle_sensor(sleep_s = .05)
            self.__toggle_sensor(sleep_s = 1)
            reading += machine.time_pulse_us(self.echo, 1, 30000)
        reading /= times
        return reading
    
    def __toggle_sensor(self, sleep_s: float = 0) -> None:
        sleep(sleep_s)
        self.trigger.toggle()

