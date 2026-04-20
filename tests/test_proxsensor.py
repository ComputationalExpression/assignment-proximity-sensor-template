import json
from unittest.mock import patch
from main import main, send_measure
from measurements import Measurements
from sensor import ProxSensor

def test_proxsensor_pulse():
    prox = ProxSensor()
    trip = prox.pulse(times = 4)
    assert trip == 12380

def test_main_exec_correct_answer(capsys):
    main()
    out, _ = capsys.readouterr()
    out = [line for line in out.strip().split("\n")]
    assert out == [
        'Object is:', 
        '* 6.98 feet away', 
        '* 2.13 meters away'
    ]

def test_main_exec_no_error(capsys):
    main()
    _, err = capsys.readouterr()
    assert err == ''

def test_API_incorrect_value():
    outcome = send_measure(
        1.10
    )
    assert outcome == {
        "id": -1,
        "accepted": False
    }

def test_API_correct_value():
    outcome = send_measure(
        3.15
    )
    assert outcome == {
        "id": 4,
        "accepted": True
    }

def test_correct_measurements():
    m = Measurements(12380)
    assert m.feet == 6.97883125434063
    assert m.meters == 2.127147766323024