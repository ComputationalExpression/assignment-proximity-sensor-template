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
    """
        Recieves measurement and sends to verification API: https://dev.chompe.rs/submit-measure
        using one parameter: value (the distance in feet)
    """

def main():
    # Connect to internet network
    connect()
    # Create btn at Pin 15, when pressed take a reading from the sensor object,
    # and pass to Measurements to get measurements.

if __name__ == "__main__":
    main()
