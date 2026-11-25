class Employee:

    def __init__(self, name, salary):
        self._name = name
        self.salary = salary

    @property # property es un decorador que permite definir un método como una propiedad de la clase, lo que significa que se puede acceder a él como si fuera un atributo, sin necesidad de llamar al método explícitamente.
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter # Este me
    def salary(self, value):
        if value < 0:
            raise ValueError("El salario no puede ser negativo")

        self._salary = value

    def promote(self, percentage):
        amount = self.salary * percentage / 100
        self.salary += amount


#employee = Employee("Ana", -1000)
employee = Employee("Ana", 1000)

print("Employee:", employee.name)
print("Current salary:", employee.salary)

employee.promote(10)

print("New salary:", employee.salary)