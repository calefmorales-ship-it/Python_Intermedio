class Animal:
    def __init__(self, nombre):
        self.nombre = nombre


    def speak(self):
        return "Hace un sonido"

class Dog(Animal):
    def speak(self):
        return "Guau"

class Cat(Animal):
    def speak(self):
        return "Miau"

dog = Dog("Duke")
cat = Cat("Candy")


print(F"{dog.nombre} dice: {dog.speak()}")
print(F"{cat.nombre} dice: {cat.speak()}")
