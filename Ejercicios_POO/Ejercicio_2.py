class Person:
    def __init__(self, name):
        self.name = name

print('Personas creadas:')
person1 = Person("Alice")
person2 = Person("Bob")
person3 = Person("Charlie")
person4 = Person("David")
person5 = Person("Eve")

print(person1.name)
print(person2.name)
print(person3.name)
print(person4.name)
print(person5.name)

class Bus:
    def __init__(self, max_passengers): #constructor que recibe el número máximo de pasajeros y crea una lista vacía para almacenar los pasajeros
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} subió al bus.")
        else:
            print("El bus está lleno.")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} bajó del bus.")
        else:
            print(f"{person.name} no está en el bus.")  

bus1 = Bus(4) # Bus con capacidad para 4 pasajeros
bus1.add_passenger(person1)
bus1.add_passenger(person2) 
bus1.add_passenger(person3)
bus1.add_passenger(person4) #limite de pasajeros alcanzado
bus1.add_passenger(person5) # pasajero no puede subir al bus porque está lleno 
bus1.remove_passenger(person3) # Remover un pasajero que está en el bus
bus1.add_passenger(person5) # Agregar un pasajero después de que uno se ha bajado
bus1.remove_passenger(person3) # Intentar remover un pasajero que ya no está en el bus


