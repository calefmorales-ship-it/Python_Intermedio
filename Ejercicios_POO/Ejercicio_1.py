class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14159 * (self.radius ** 2)

my_area = Circle(20)
print(f"Area of the circle with radius {my_area.radius}: {my_area.get_area()}")