"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    engine = None

    def set_engine(volume, pistons):
        temp_engine = Engine(volume=volume, pistons=pistons)
        return temp_engine
