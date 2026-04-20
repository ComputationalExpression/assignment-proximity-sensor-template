class Measurements:

    def __init__(self, reading: float):
        self.feet = self.__distance_in_feet(reading)
        self.meters = self.__distance_in_meters(reading)

    def __distance_in_feet(self, reading: float) -> float:
        """ Takes a reading and returns the distance in feet """

    def __distance_in_meters(self, reading: float) -> float:
        """ Takes a reading and returns the distance in meters """

    def __distance_in_cm(self, reading: float) -> float:
        """ Uses formula in README to convert a reading to centimeters """
    
    def __str__(self):
        return f"""Object is:
* {round(self.feet, 2)} feet away
* {round(self.meters, 2)} meters away"""
