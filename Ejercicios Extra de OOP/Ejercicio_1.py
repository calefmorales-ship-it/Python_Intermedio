class Rectangle:
    def __init__(self, width, height): #constructor de la clase Rectangle que recibe el ancho y la altura del rectángulo
        if width < 0 or height < 0: # verifica si el ancho o la altura son negativos y lanza una excepción si es así
            raise ValueError( # lanza una excepción con un mensaje de error
                "Existe un valor negativo, los valores deben ser positivos"
            )

        self.width = width
        self.height = height

    def get_area(self): # metodo para calcular el área del rectángulo
        return self.width * self.height

    def get_perimeter(self):# metodo para calcular el perímetro del rectángulo
     return 2 * (self.width + self.height)


while True:
    try:
        input_width = int(input("Enter the width of the rectangle: "))
        input_height = int(input("Enter the height of the rectangle: "))

        rect = Rectangle(input_width, input_height)

        break

    except ValueError as error:
        print(error)
        print("Please enter valid values.\n")


rect = Rectangle(input_width, input_height)# instancia de la clase Rectangle con los valores ingresados por el usuario

print("Area of the rectangle:", rect.get_area())# objeto rect llama al método get_area() para calcular el área del rectángulo y se imprime el resultado
print("Perimeter of the rectangle:", rect.get_perimeter())  # objeto rect llama al método get_perimeter() para calcular el perímetro del rectángulo y se imprime el resultado 