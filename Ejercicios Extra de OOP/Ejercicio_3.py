
class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount


class Inventory:
    def __init__(self):
        self.products = [] #se inicializa una lista vacía para almacenar los productos en el inventario

    def add_product(self, product): #se define el método para agregar un producto al inventario de la lista de productos
        self.products.append(product)

    def show_products(self):# muestra los productos en el inventario, si no hay productos, imprime un mensaje indicando que no hay productos en el inventario
        if not self.products:
            print("No products in inventory.")
            return

        for product in self.products:
            print(
                f"Product: {product.name}, "
                f"Price: {product.price}, "
                f"Amount: {product.amount}"
            )

    def calculate_total_value(self): #calcula el valor total del inventario multiplicando el precio de cada producto por su cantidad y sumando los resultados
        return sum(product.price * product.amount for product in self.products)


product1 = Product("Mouse", 5000, 3)# se crea una instancia de la clase Product con nombre "Mouse", precio 5000 y cantidad 3
product2 = Product("Teclado", 8000, 2)# se crea una instancia de la clase Product con nombre "Teclado", precio 8000 y cantidad 2

inventory = Inventory() #se crea una instancia de la clase Inventory

inventory.add_product(product1)# se agrega el producto 1 a la lista de productos del inventario
inventory.add_product(product2)# se agrega el producto 2 a la lista de productos del inventario

print("All products:")
inventory.show_products()

print(f"Total inventory value: {inventory.calculate_total_value()}") #31000
