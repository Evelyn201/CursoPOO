from Python.car import Car
from car import Car

class UberVan(Car):
    typeCarAccepted = []
    seatsMaterial = []

    def __init__(self, license, driver,typeCarAccepted,seatsMaterial):
        super().__init__(license, driver)
        self.__init__(license,driver)
        self.seatsMaterial = seatsMaterial
