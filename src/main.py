import json

import network
import details
import requests

from time import sleep
from machine import Pin
from sensor import ProxSensor
from measurements import Measurements

def connect():
    env = details.load_dotenv()
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(env["SSID"], env["PASS"])
    while not wlan.isconnected():
        sleep(1)
    #print(f"Connected to: {env['SSID']}")

def send_measure(measurement: float):
    response = requests.post(
        "https://dev.chompe.rs/submit-measure",
        json={
            "value": measurement
        }
    ).text
    return json.loads(response)

def main():
    # Connect to internet network
    connect()
    btn = Pin(15, Pin.IN, Pin.PULL_UP)
    sensor = ProxSensor()
    while True:
        if btn.value() == 0:
            distance = sensor.pulse(times = 3)
            break
    units = Measurements(distance)
    print(units)
    send_measure(measurement = units.feet)

if __name__ == "__main__":
    main()