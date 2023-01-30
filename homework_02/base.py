from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started: bool = False
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
                raise LowFuelError

    def move(self, distance):
        fuel_for_dist = distance * self.fuel_consumption
        if fuel_for_dist <= self.fuel:
            self.fuel = self.fuel - fuel_for_dist
            return self.fuel
        else:
            raise NotEnoughFuel
