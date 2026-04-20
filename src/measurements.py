class Measurements:

    def __init__(self, reading: float):
        self.feet = self.__distance_in_feet(reading)
        self.meters = self.__distance_in_meters(reading)

    def __distance_in_feet(self, reading: float) -> float:
        cm = self.__distance_in_cm(reading)
        if (cm <= 0):
            return 0
        return (cm / 2.54) / 12

    def __distance_in_meters(self, reading: float) -> float:
        return self.__distance_in_cm(reading) / 100

    def __distance_in_cm(self, reading: float) -> float:
        return (reading / 2) / 29.1
    
    def __str__(self):
        return f"""Object is:
* {round(self.feet, 2)} feet away
* {round(self.meters, 2)} meters away"""