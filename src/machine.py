import time
import random
from typing import Any

class Pin:

    IN = 0
    OUT = 1
    PULL_UP = 1

    def __init__(self, id: Any, mode: Any, *args, **kwargs):
        self.id = id
        self.mode = mode
        self.val = 0

    def value(self, value: int = 0) -> int:
        time.sleep(1)
        self.val = value
        return self.val
      
    def on(self):
        pass

    def off(self):
        pass

    def toggle(self):
        self.val = 0 if self.val == 1 else 1

def time_pulse_us(echo: Pin, pulse_level, timeout_us) -> int:
    return 12380