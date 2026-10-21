class Rectangle:
    def __init__(self, width, height):#constructor de la clase Rectangle que recibe el ancho y la altura del rectángulo
        self.width = width
        self.height = height

    def area(self): # metodo para calcular el área del rectángulo
        return self.width * self.height 

    def perimeter(self):# metodo para calcular el perímetro del rectángulo
        return 2 * (self.width + self.height)

while True:  
    try:
        input_width = int(input("Enter the width of the rectangle: "))
        input_height = int(input("Enter the height of the rectangle: "))

        if input_width < 0 or input_height < 0:
            print("Existe un valor negativo, los valores deben ser positivos.")
            continue

        break

    except ValueError:
        print("Please enter valid numbers.")

rect = Rectangle(input_width, input_height)# instancia de la clase Rectangle con los valores ingresados por el usuario

print("Area of the rectangle:", rect.area())# objeto rect llama al método area() para calcular el área del rectángulo y se imprime el resultado
print("Perimeter of the rectangle:", rect.perimeter())  # objeto rect llama al método perimeter() para calcular el perímetro del rectángulo y se imprime el resultado 