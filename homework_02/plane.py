"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = None

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo

    def load_cargo(self, new_cargo):
        temp_cargo = self.cargo + new_cargo
        if temp_cargo <= self.max_cargo:
            self.cargo = temp_cargo
            return self.cargo
        else:
            raise CargoOverload
