from account import Account

class Car:
    id             = int
    license        = str
    driver         = Account ("","")
    passeggenger   = int

    def __init__(self, license, driver):
        self.license      = license
        self.driver       = driver