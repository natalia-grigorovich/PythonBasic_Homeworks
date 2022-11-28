from abc import ABC
from homework_02.exceptions import LowFuelError


class Vehicle(ABC):
    #started: bool = bool()
    started = bool()
    weight = None
    fuel = None
    fuel_consumption = None
    
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
                return self.started
            else:
                raise LowFuelError('LowFuelError')
