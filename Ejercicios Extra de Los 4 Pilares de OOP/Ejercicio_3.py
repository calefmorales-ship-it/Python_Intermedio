class Vehicle:

    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return f"{self._brand} ({self._year})"


class Car(Vehicle):

    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self._doors = doors

    def get_info(self):
        return f"{super().get_info()} - Puertas: {self._doors}"


class Motorcycle(Vehicle):

    def __init__(self, brand, year, motorcycle_type):
        super().__init__(brand, year)
        self._motorcycle_type = motorcycle_type

    def get_info(self):
        return f"{super().get_info()} - Tipo: {self._motorcycle_type}"


vehicle1 = Car("Toyota", 2020, 4)
vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")

print(vehicle1.get_info())
print(vehicle2.get_info())