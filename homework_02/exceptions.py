"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    print('LowFuelError')


class NotEnoughFuel(Exception):
    pass


class CargoOverload(Exception):
    pass
