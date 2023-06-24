from car import Car

class UberBlack(Car):
    typeCarAccepted = []
    seatsMateriaal = []

    def __init__(self, license, driver, typeCarAccepted, seatsMaterial):
        super().__init__(license, driver)
        self.typeCarAccepted = typeCarAccepted
        self. seatsMateriaal = seatsMaterial