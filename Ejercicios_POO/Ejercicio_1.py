class Circle:
    radius = 20

    def get_area(self):
        return 3.14159 * (self.radius ** 2)

my_area = Circle()
print(f"Area of the circle with radius {my_area.radius}: {my_area.get_area()}")